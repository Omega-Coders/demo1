from django.http import HttpResponse
from django.shortcuts import render

def demofunc(request):
    return HttpResponse('mahesh')
