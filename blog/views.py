from django.shortcuts import render_to_response
from blog.models import posts
from blog.models import AboutMe
from django.http import HttpResponse
import datetime


def home(request):
    aboutmetext = AboutMe.objects.all()[:1]
    return render_to_response('blog/home.html', {'AboutMe': aboutmetext})


def blog(request):
    entries = posts.objects.all()[:10]
    return render_to_response('blog/blog.html', {'posts': entries})

