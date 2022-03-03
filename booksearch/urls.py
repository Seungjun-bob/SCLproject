from django.urls import path, include
from . import views

app_name = 'booksearch'
urlpatterns = [
    path('', views.booksearch, name='booksearch'),
]