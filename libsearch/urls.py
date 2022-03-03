from django.urls import path, include
from . import views

app_name = 'libsearch'
urlpatterns = [
    path('', views.libsearch, name='libsearch'),
]
