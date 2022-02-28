from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('index.urls')),
    path('account/', include('account.urls')),
    path('libsearch/', include('libsearch.urls')),
    path('booksearch/', include('booksearch.urls')),
    path('recommend/', include('recommend.urls')),
    path('board/', include('board.urls'))
]
