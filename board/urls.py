from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.board, name='board'),
    path('myreview/', views.my_review, name='myreview'),
    path('submit/', views.submit, name='submit'),
    path('result/', views.result, name='result'),
]
