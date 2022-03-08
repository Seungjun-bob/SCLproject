from django.urls import path, include
from . import views
app_name = 'board'
urlpatterns = [
    path('', views.board, name='board'),
    path('myreview/', views.my_review, name='myreview'),
    path('submit/', views.submit, name='submit'),
    path('<int:pk>', views.result, name='result'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comment, name='comments')
]
