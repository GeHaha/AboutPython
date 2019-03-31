

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

#request 是一个用户的url访问

def hello(request):
    return HttpResponse("Hello world! I am coming...")







