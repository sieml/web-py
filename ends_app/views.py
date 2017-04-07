import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template import RequestContext

from ends_app.models import Article


def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    return render(request, 'index.html', {"blogs": blogs})


def say_hello(request):
    s = 'Hello World!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)
