from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Faculty

class FacultyCreateView(CreateView):
    model = Faculty
    fields = ['first_name', 'last_name', 'subject','mobile','email']
    template_name = 'faculty_form.html'  # Optional: specify custom template
    success_url = reverse_lazy('faculty_list')  # URL to redirect to after successful form submission

class FacultyListView(ListView):
    model = Faculty
    context_object_name = 'faculties'  # Optional: specify the context variable name in templates
    template_name = 'faculty_list.html'  # Optional: specify custom template

class FacultyUpdateView(UpdateView):
    model = Faculty
    fields = ['first_name', 'last_name', 'subject','mobile','email']
    template_name = 'faculty_form.html'  # Optional: specify custom template
    success_url = reverse_lazy('faculty_list')  # URL to redirect to after successful form submission

class FacultyDeleteView(DeleteView):
    model =Faculty
    template_name = 'faculty_confirm_delete.html'  # Optional: specify custom template
    success_url = reverse_lazy('faculty_list')  # URL to redirect to after successful deletion

