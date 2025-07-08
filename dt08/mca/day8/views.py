from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import StudentModel
from .forms import StudentForm
def insert_student(request):
    context={}
    ob_form =StudentForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['from']=ob_form
    return render(request, "insert_student.html",context)
