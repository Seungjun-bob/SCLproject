from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.libsearch, name='libsearch'),
]
