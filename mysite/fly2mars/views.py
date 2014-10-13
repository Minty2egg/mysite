from django.shortcuts import render
from django.template import Context,RequestContext
from django.template.loader import get_template
from django.http import *
from django.contrib.auth import *
# Create your views here.

def fly2mar(request):
	#t = get_template('fly2mars.html')
	t = get_template('index.html')
	logined = user_Auth(request)
	html = t.render(RequestContext({'fly2mars':1,'logined':logined}))
	return HttpResponse(html)

def index(request):
	#t = get_template('index.html')
	logined ,username= user_Auth(request)
	#html = t.render(RequestContext({'fly2mars':0,'logined':logined}))
	return render(request,'index.html',{'fly2mars':0,'logined':logined,'username':username})

	#return HttpResponse(html)
	
def user_Auth(request):
	if request.method == 'POST':
		username = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return True,username
	return False,None
	