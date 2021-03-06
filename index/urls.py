from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mypage/', views.mypage, name='mypage'),
    path('user_del/', views.user_del, name='user_del'),
    path('update/', views.changepassword, name='update'),
]
