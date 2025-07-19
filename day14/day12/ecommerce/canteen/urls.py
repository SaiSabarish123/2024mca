from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('menu/<int:pk>/', views.menu_detail, name='menu_detail'),
    path('add/', views.add_menu_item, name='add_menu_item'),
    path('cart/add/<int:menu_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('delete/<int:pk>/', views.delete_menu_item, name='delete_menu_item'),
]
