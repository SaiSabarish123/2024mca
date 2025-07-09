from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
def page1(request):
    return render(request,  'arun.html')

def page2(request):
    return render(request,  'ashok.html')

def page3(request):
    return render(request,  'tharun.html')

def page4(request):
    return render(request,  'yeshwanth.html')
