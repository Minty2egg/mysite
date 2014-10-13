from django.conf.urls.defaults import *
from mysite.books import models, views

urlpatterns + =[
	url(r'^publisher/$',views.display_models,{'model':models.Publisher}),
	url(r'^author/$',views.display_models,{'model':models.Author}),
	
]