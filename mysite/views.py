# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
import datetime
from packages import dhello


def current_url_view(request):
	return HttpResponse('Welcome to the page at %s' % request.path)
	
def display_meta(request):
	values = request.META.items()
	values.sort()
	value1 = ()
	value2 = ()
	for k,v in values:
		value1 = value1 + (k,)
		value2 = value2 + (v,)
	t = get_template('base.html')
	#html = t.render(Context({'value1':value1},{'value2':value2},))
	html = t.render(Context({'values':values}))
	return HttpResponse(html)
	
def display_meta1(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
    	
def hello(request):
	t = get_template('base.html')
	now = datetime.datetime.now()
	d = dhello(1,now)
	html = t.render(Context({'d':d}))
	return HttpResponse(html)
    
def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body><center>It's now %s.</center></body></html>" % (now)
	return HttpResponse(html)
	
def hours_ahead(request, offset, day):#
	try:
		offset = int(offset)
		day = str(day)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() +datetime.timedelta(hours= offset)
	html = "<html><body><center>In %s hour(s), it will be %s, after %s day.</center></body></html>" % (offset,dt,day)
	return HttpResponse(html)#