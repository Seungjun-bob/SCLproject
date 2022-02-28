from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.board),
    path('myreview/', views.my_review),
    path('submit/', views.submit)
]
