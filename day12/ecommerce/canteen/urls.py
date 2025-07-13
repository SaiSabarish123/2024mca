from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/add/', views.add_menu_item, name='add_menu_item'),
    path('menu/<int:menu_id>/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('menu/<int:pk>/', views.menu_detail, name='menu_detail'),
    path('menu/<int:pk>/delete/', views.delete_menu_item, name='delete_menu_item'),
]
