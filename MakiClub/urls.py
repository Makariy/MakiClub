from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('', include('authorization.urls')),
    path('recipes/', include('recipes.urls')),
    path('groups/', include('groups.urls')),
    path('search/', include('search.urls')),

    path('admin/', admin.site.urls),
]
