from django.shortcuts import render

def shop(request):
    return render(request, 'adv/shop.html')


def vacanse(request):
    return render(request, 'adv/vacanse.html')


