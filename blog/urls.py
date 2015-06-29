from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from . import views
from blog.models import posts

urlpatterns = patterns('',
                       url(r'^$', 'blog.views.home', name='home'),
                       url(r'^blog/$', 'blog.views.blog', name='blog'),
                       url(r'^latestnews/$', 'blog.views.latestnews', name='latestnews'),
                       url(r'^archive/$', 'blog.views.archive', name='archive'),

                       url(r'^(?P<pk>\d+)$', DetailView.as_view(
                           model=posts,
                           template_name="oneperpage.html"))
                       )