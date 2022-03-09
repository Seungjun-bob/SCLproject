from django.urls import path
from . import views

app_name = 'recommend'
urlpatterns = [
    path('', views.recommend, name='recommend'),
    path('<int:recommend_id>/', views.detail_recom, name='detail_r'),
    path('<int:recommend_id>/comments/', views.comment_create, name='comment_create'),
    path('<int:recommend_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete')
]