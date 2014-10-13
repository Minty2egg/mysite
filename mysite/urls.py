
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello,current_datetime,hours_ahead,current_url_view,display_meta
#import mysite.books.views
from mysite.books import views,models
#from mysite.fly2mars import views as fmv
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^fly2mars/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_URL}),
    url(r'search-form',views.search),
    url(r'search',views.search),
    url(r'^url/',display_meta),
    url(r'^plus/(\d{1,2})(\d{1})/$',hours_ahead),
	url(r'^hello/',hello),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$',views.contact),
    url(r'^contact/thanks/$',views.thanks),
    
]

urlpatterns += [
	url(r'^fly2mars/','mysite.fly2mars.views.index'),
	url(r'^$','mysite.fly2mars.views.index'),
    #url(r'^$',fmv.index),
    #url(r'^fly2mars/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
]

urlpatterns += [
	url(r'^publisher/$',views.display_models,{'model':models.Publisher}),
	url(r'^author/$',views.display_models,{'model':models.Author}),
	
]

urlpatterns += [
	url(r'^weixin/$','mysite.weixin.views.weixin'),
	url(r'^weixindebug/$','mysite.weixin.views.weixinDebug'),
]