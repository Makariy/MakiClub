from django.urls import path
from .views import search_view


urlpatterns = [
    path('get/', search_view, name='search_get'),
]

