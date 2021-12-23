from django.urls import path

from .views import ajax_get_recipe_best_month
from .views import ajax_get_recipe_best_today


urlpatterns = [
    path('get/best_today/', ajax_get_recipe_best_today, name='get_presentation'),
    path('get/best_month/', ajax_get_recipe_best_month, name='get_popular'),
]
