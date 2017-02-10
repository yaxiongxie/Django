from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Question


def list(reqest):
    data_list = Question.objects.all()
    context = {'data_list': data_list}
    return render(reqest, 'polls/index2.html', context)
