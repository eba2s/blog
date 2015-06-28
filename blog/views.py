from django.shortcuts import render_to_response
from blog.models import posts
from django.http import HttpResponse
import datetime


# Create your views here.


# def home(request):
# entries = posts.objects.all()[:10]
#     html = "<html><body> %  % </body></html"
#     return render_to_response("blog.html", {'posts: entries'})
#
# def home(request):
#     # entries = posts.objects.all()[:10]
#     return render_to_response('index.html', {'posts': entries})


# Create your views here.

def home(request):
    return render_to_response('blog/index.html')


def blog(request):
    entries = posts.objects.all()[:10]
    return render_to_response('blog/blog.html', {'posts': entries})

    # blog = posts.objects.all()[:10]
    # html = "<html><body>  </body></html" % blog
    # return HttpResponse("blog.html", {'posts: entries'})
