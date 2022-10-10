from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>welcome to django.</h1>')


def display_name(request):
    data = {"name": "vijaya kumar"}
    return render(request, 'my_app/index.html', context=data)


