from django.shortcuts import render

# Create your views here.
def vacanse(request):
    return render(request, 'vacanse/vacanse.html')