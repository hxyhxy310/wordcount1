from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse('hello')

# def home(request):
#     return HttpResponse(request,'home.html')
