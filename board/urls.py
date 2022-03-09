from django.urls import path, include
from . import views
app_name = 'board'
urlpatterns = [
    path('', views.board, name='board'),
    path('myreview/', views.my_review, name='myreview'),
    path('submit/', views.submit, name='submit'),
    path('<int:board_id>/', views.result, name='result'),
    path('<int:board_id>/delete/', views.delete, name='delete'),
    path('<int:board_id>/update/', views.update, name='update'),
    path('<int:board_id>/comments/', views.comment_create, name='comment_create'),
    path('<int:board_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete')
]
