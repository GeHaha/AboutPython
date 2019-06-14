from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# 响应url
def hello(request):
    return HttpResponse("Hello world！I am coming....")