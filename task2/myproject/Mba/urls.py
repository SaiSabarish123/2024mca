from django.urls import path
from .views import FacultyCreateView, FacultyListView 
from .views import FacultyUpdateView, FacultyDeleteView
urlpatterns = [
    path('', FacultyListView.as_view(), name='faculty_list'),
    path('create/', FacultyCreateView.as_view(), name='faculty_create'),
    path('update/<int:pk>/', FacultyUpdateView.as_view(), name='faculty_update'),
    path('delete/<int:pk>/', FacultyDeleteView.as_view(), name='faculty_delete'),
]
