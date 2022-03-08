from django.urls import path
from . import views

app_name = 'recommend'
urlpatterns = [
    path('', views.recommend, name='recommend'),
    path('detail/<int:pk>', views.detail, name='detail')
]
