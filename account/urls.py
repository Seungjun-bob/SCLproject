from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('about/', views.about),
    path('changepassword/', views.changepassword)
]
