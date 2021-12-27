from django.urls import path

from .views import ajax_get_recipe_best_month
from .views import ajax_get_recipe_best_today
from .views import ajax_get_best_feasts
from .views import ajax_get_groups
from .views import ajax_get_recipe
from .views import ajax_get_recipe_data

from .views import RecipeView


urlpatterns = [
    path('get/best_today/', ajax_get_recipe_best_today, name='get_best_today'),
    path('get/best_month/', ajax_get_recipe_best_month, name='get_best_month'),
    path('get/best_feasts/', ajax_get_best_feasts, name='get_best_feasts'),
    path('get/groups/', ajax_get_groups, name='get_groups'),
    path('get/recipe/', ajax_get_recipe, name='get_recipe'),
    path('get/recipe_data/', ajax_get_recipe_data, name='get_recipe_data'),

    path('recipe/', RecipeView.as_view(), name='recipe')
]
