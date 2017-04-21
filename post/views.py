from django.shortcuts import render, get_object_or_404

from .models import News, Vacancy, Shop


# News
def news_detail(request, id):
    context = get_object_or_404(News, pk=id)
    return render(request, 'news/detail.html', {'post': context})

def news_index(request):
    context = News.objects.all()
    return render(request, 'news/index.html', {'posts': context})

# Vacancy
def vacancy_detail(request, id):
    context = get_object_or_404(Vacancy, pk=id)
    return render(request, 'vacancy/detail.html', {'post': context})

def vacancy_index(request):
    context = Vacancy.objects.all()
    return render(request, 'vacancy/index.html', {'posts': context})

# Shop
def shop_detail(request, id):
    context = get_object_or_404(Shop, pk=id)
    return render(request, 'shop/detail.html', {'post': context})


def shop_index(request):
    context = Shop.objects.all()
    return render(request, 'shop/index.html', {'posts': context})

