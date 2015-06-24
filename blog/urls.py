from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import posts

urlpatterns = patterns('',
                       url(r'^blog/$', name='blog'),
                       )