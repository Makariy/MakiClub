from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('', include('authorization.urls')),

    path('admin/', admin.site.urls),
]
