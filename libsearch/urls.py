from django.urls import path, include
from . import views

app_name = 'libsearch'
urlpatterns = [
    path('', views.libsearch, name='libsearch'),
    path('detail_l/<int:library_id>', views.detail_library, name='detail_l'),
    path('detail_l/<int:library_id>/comments/', views.comment_create, name='comment_create'),
    path('detail_l/<int:library_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete')
]
