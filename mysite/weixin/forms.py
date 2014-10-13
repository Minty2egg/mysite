from django import forms

class weixinForm(forms.Form):
	fromu = forms.CharField(max_length=100)
	tou = forms.CharField(max_length=100)
	msg_type = forms.CharField(max_length=100)
	event = forms.CharField(max_length = 100)
	message = forms.CharField(widget = forms.Textarea)

class RedirectInfomation(object):
	def __init__(self,flag,info):
		self.redirect = flag
		self.infomation = info
