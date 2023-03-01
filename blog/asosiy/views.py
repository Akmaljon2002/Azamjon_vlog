from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    data = {
        'maqolalar':Maqola.objects.all()
    }
    return render(request, 'blog.html', data)

def intervyular(request):
    data = {
        'intervyular':Intervyu.objects.all()
    }
    return render(request, 'intervyular.html', data)

def maqola(request, son):
    data = {
        'maqola':Maqola.objects.get(id=son)
    }
    return render(request, 'maqola.html', data)

def intervyu(request, son):
    data = {
        'intervyu':Intervyu.objects.get(id=son)
    }
    return render(request, 'intervyu.html', data)