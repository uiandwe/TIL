
$sudo pip3 install uwsgi

$sudo apt-get install uwsgi-plugin-python

# hello.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"] # python3
    #return ["Hello World"] # python2
    
    
$ uwsgi --http-socket :8000 --plugin python --wsgi-file hello.py



# views.py
# -*- coding: utf-8 -*-
from django.http import HttpResponse
 
 
def greeting(request):
    return HttpResponse(‘Hello Yonghee. 쟝고가 잘 돌고 있는것 같아요’)
    
    
    
#urls.py
from django.conf.urls import patterns, include, url
from django.contrib import admin
from myFirstWebApp import views
 
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', views.greeting, name='greeting'),
)




