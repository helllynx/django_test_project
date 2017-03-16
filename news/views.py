from django.shortcuts import render

from .models import News

def detail(request,iq):
    return render(request, 'home/index.html')

def news(request):
    posts = News.objects.all()
    return render(request, 'news/index.html', {'posts':posts})
