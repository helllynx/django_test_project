from django.shortcuts import render, get_object_or_404
from .models import Shop


def detail(request, id):
    shop = get_object_or_404(Shop, pk=id)
    return render(request, 'shop/detail.html', {'post': shop})


def index(request):
    shop = Shop.objects.all()
    return render(request, 'shop/index.html', {'posts': shop})
