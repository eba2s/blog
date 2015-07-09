from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.views import One_Per_Page
from blog.views import Blog_Per_Page


urlpatterns = patterns('',
                       url(r'^$', 'blog.views.home', name='home'),
                       url(r'^blog/$', 'blog.views.blog', name='blog'),
                       url(r'^latestnews/$', 'blog.views.latestnews', name='latestnews'),
                       url(r'^archive/$', 'blog.views.archive', name='archive'),

                       url(r'^(?P<pk>\d+)/', One_Per_Page.as_view(
                           template_name='blog/aboutme_detail.html'), name="detail"),

                       url(r'^blog/(?P<pk>\d+)/', Blog_Per_Page.as_view(
                           template_name='blog/blogpost_detail.html'), name="detail"),

                       url(r'^latestnews/(?P<pk>\d+)/', Blog_Per_Page.as_view(
                           template_name='blog/blogpost_detail.html'), name="detail"),

                       url(r'^archive/(?P<pk>\d+)/', Blog_Per_Page.as_view(
                           template_name='blog/blogpost_detail.html'), name="detail")





                       )