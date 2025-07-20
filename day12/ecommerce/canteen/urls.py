from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.master, name='master'),

    path('home/',views.home, name='home'),
    path('menu', views.menu_list, name='menu_list'),
    path('menu/<int:pk>/', views.menu_detail, name='menu_detail'),
    path('add/', views.add_menu_item, name='add_menu_item'),
    path('cart/add/<int:menu_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('delete/<int:pk>/', views.delete_menu_item, name='delete_menu_item'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
