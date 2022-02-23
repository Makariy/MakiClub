from django.urls import path
from .views import SearchView
from .views import ajax_search


urlpatterns = [
    path('', SearchView.as_view(), name='search'),
    path('get/', ajax_search, name='search_get'),
]

