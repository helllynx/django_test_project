from django.http import Http404
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext

from .models import News


def detail(request, id):
    news = News.objects.get(pk=id)
    return render(request, 'news/detail.html', {'post': news})



def news(request):
    posts = News.objects.all()
    return render(request, 'news/index.html', {'posts':posts})
