from django.urls import path
from . import views
urlpatterns = [
   path('insert_employee/',views.insert_employee,name='insert_employee'),
   path('add_number/',views.add_number, name='add_number'),
]
