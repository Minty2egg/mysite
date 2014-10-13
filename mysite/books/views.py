from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from mysite.books.models import Book
from django.template.loader import get_template
from django.template import Context
from mysite.books.forms import ContactForm,RedirectInfomation

def search_form(request):
	return render_to_response('search_form.html')
# Create your views here.

def search(request):	
	t = get_template('search_form.html')
	html = t.render(Context({'error':False}))
	#context = {'error':True}
	if 'q' in request.GET:
		q = request.GET['q'] 
		if q:
			books = Book.objects.filter(title__icontains=q)
			html = t.render(Context({'books':books,'query':q,'error':False}))
		else:
			html = t.render(Context({'error':True,'query':q}))
	#else:
	#	html = t.render(Context({'error':True}))
	return HttpResponse(html)

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial = {'subject':'I love this site.','email':'example@example.com'}
		)
	return render(request,'contact_form.html',{'form':form,'weixin':False})

def thanks(request):
	t = get_template('base.html')
	rd = RedirectInfomation(True,'Submitted.')
	html = t.render(Context({'d':rd}))
	return HttpResponse(html)
	
def display_models(request,model):
	html = "%s,%s" % (model.__name__,model.__name__.lower())
	return HttpResponse(html)