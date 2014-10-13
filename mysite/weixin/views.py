from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import xml.etree.ElementTree as ET
from django.template import Context
from django.template.loader import get_template
import time 
from mysite.weixin.forms import weixinForm
# Create your views here.

welcome_text = 'Welcom!'
class wxResponse(object):
	def __init__(self,tou='',fromu='',content='',msg_type='',time=''):
		self.tou = tou
		self.fromu = fromu
		self.content = content
		self.msg_type = msg_type
		self.time = time
	def fillResponse(self):
		xml = "<xml><ToUserName>%s</ToUserName> \
		<FromUserName>%s></FromUserName>\
<CreateTime>%s</CreateTime>\
<MsgType>%s</MsgType>	\
<Content>%s</Content>\
<FuncFlag>0</FuncFlag>\</xml>"	% (self.tou,self.fromu,self.time,self.msg_type,self.content)
		return xml
		
def process_message(xml,msg_type):
	#t = get_template('weixin.xml')
	message = wxResponse()
	tou = xml.find('ToUserName').text
	fromu = xml.find('FromUserName').text
	#tou = xml['tou']
	#fromu = xml['fromu']
	#msg_type = xml['msg_type']
	if msg_type == 'event':
		event = xml.find('Event').text
		#event = xml['event']
		if event == 'subscribe':
			message.content = welcome_text
	elif msg_type =='text':
		content = xml.find('Context').text
		#msg = xml['message']
		message.content = msg
	else:
		message.content = welcome_text
	message.tou = fromu
	message.fromu = tou
	message.msg_type = msg_type
	message.time = str(int(time.time()))
	#xml = t.render(Context({'weixin':message}))
	xml = message.fillResponse()
	return HttpResponse(xml)
		
def get_message(message):
	xml_rec = ET.fromstring(message)
	msg_type = xml_rec.find('MsgType').text
	#msg_type = message['msg_type']
	return process_message(xml_rec,msg_type)
	
def weixin(request):
	if request.method == 'GET':
		data = request.GET
		echostr = data.get('echostr','')
		return HttpResponse(echostr)
	else:
		message = ''
		for item in request.readlines():
			message += str(item)
		return get_message(message)
		
def weixinDebug(request):
	if request.method == 'POST':
		form = weixinForm(request.POST)
	else:
		form = weixinForm(
			initial={}
		)
	return render(request,'contact_form.html',{'form':form,'weixin':True})