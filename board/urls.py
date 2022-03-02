from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.board, name='board'),
    path('myreview/', views.my_review, name='myreview'),
    path('submit/', views.submit, name='submit'),
    path('result/', views.result, name='result')
]
