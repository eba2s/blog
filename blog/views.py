from django.shortcuts import render_to_response
from blog.models import posts
from blog.models import AboutMe
from django.http import HttpResponse, Http404
from django.views.generic import DetailView
from django.core.urlresolvers import reverse


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
    model = AboutMe


class Blog_Per_Page(DetailView):
    model = posts


    # def get_absolute_url(self):
    # return reverse('entry_detail', kwargs={'pk': self.pk})

    # def oneperpage(request):
    #     entry = One_Per_Page.objects.get_queryset(pk=AboutMe.id)
    #     entry = super(One_Per_Page).get_queryset()
    #     return render_to_response('blog/aboutme_detail.html', {'AboutMe': entry})