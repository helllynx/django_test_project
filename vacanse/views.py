from django.shortcuts import render, get_object_or_404

from .models import Vacanse


def detail(request, id):
    vac = get_object_or_404(Vacanse, pk=id)
    return render(request, 'vacanse/detail.html', {'post': vac})


def index(request):
    vac = Vacanse.objects.all()
    return render(request, 'vacanse/index.html', {'posts': vac})
