from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def red(request):
    stu=[{'name':'Thriven','marks':90},{'name':'Srikar','marks':88},
           {'name':'Tharun','marks':85},{'name':'Roopesh','marks':99}]
    return render(request,'red.html',{'data': stu})
