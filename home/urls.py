from django.urls import path

from .views import ajax_get_recipe_presentation
from .views import ajax_get_recipe_popular

from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('get/presentation/', ajax_get_recipe_presentation, name='get_presentation'),
    path('get/popular/', ajax_get_recipe_popular, name='get_popular'),
]
