from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from . import views
from blog.models import posts

urlpatterns = patterns('',
                       url(r'^$', 'blog.views.home', name='home'),
                       url(r'^blog/$', 'blog.views.blog', name='blog'),
                       )