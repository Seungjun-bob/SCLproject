from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('login/', views.login, name='login'),
]
