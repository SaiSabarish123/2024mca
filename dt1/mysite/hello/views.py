from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    return HttpResponse('Hello,Django!')


def demo(request):
    temp=loader.get_template('ind.html')
    return HttpResponse(temp.render())
