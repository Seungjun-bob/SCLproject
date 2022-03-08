from django.urls import path, include
from . import views

app_name = 'libsearch'
urlpatterns = [
    path('', views.libsearch, name='libsearch'),
    path('detail_l/<int:pk>', views.detail_library, name='detail_l')
]
