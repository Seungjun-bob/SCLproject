from django.urls import path
from . import views

app_name = 'recommend'
urlpatterns = [
    path('', views.recommend, name='recommend'),
    path('detail_r/<int:pk>', views.detail_recom, name='detail_r'),
    path('<int:pk>/comments/', views.detail_comment, name='comments_r')
]
