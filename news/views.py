from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext

from .models import News


def detail(request, id):
    news = get_object_or_404(News, pk=id)
    return render(request, 'news/detail.html', {'post': news})


def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'posts': news})
