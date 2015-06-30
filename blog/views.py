from django.shortcuts import render_to_response
from blog.models import posts
from blog.models import AboutMe
from django.views.generic import DetailView

from django.http import HttpResponse
import datetime


def home(request):
    entries = AboutMe.objects.all()[:1]
    guest = posts.objects.all()[:3]
    return render_to_response('blog/home.html', {'AboutMe': entries, 'posts': guest})


def blog(request):
    entries = posts.objects.all()[:10]
    return render_to_response('blog/blog.html', {'posts': entries})


def latestnews(request):
    entries = posts.objects.all()[:3]
    return render_to_response('blog/latestnews.html', {'posts': entries})

def archive(request):
    entries = posts.objects.all()
    return render_to_response('blog/latestnews.html', {'posts': entries})


class One_Per_Page(DetailView):
    queryset = posts.objects.all()


    def oneperpage(self):
        entries = super(One_Per_Page, self).get_queryset()
        return render_to_response('blog/posts_detail.html', {'posts': entries})