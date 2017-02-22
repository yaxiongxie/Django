from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Rent


def list(reqest):
    data_list = Rent.objects.all()
    context = {'data_list': data_list,"nav_flag":2}
    return render(reqest, 'polls/index2.html', context)


def detail(request):
    context = {"nav_flag": 2}
    return render(request, 'polls/detail.html',context)


def aboutus(request):
    context = {"nav_flag": 5}
    return render(request, 'polls/aboutus.html',context)


def index(request):
    context = {"nav_flag": 1}
    return render(request, 'polls/index.html',context)


def services(request):
    context = {"nav_flag": 4}
    return render(request, 'polls/services.html',context)
