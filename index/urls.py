from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'index'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.index, name='index'),
    ]
