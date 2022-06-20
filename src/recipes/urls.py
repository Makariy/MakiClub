from django.urls import path

from .views import recipe_image_view
from .views import recipe_preview_view

from .views import get_recipe_best_month_view
from .views import get_recipe_best_today_view
from .views import get_best_feasts_view
from .views import get_groups_view
from .views import get_recipe_view
from .views import get_recipe_data_view


urlpatterns = [
    path('get/best_today/', get_recipe_best_today_view, name='get_best_today'),
    path('get/best_month/', get_recipe_best_month_view, name='get_best_month'),
    path('get/best_feasts/', get_best_feasts_view, name='get_best_feasts'),
    path('get/groups/', get_groups_view, name='get_groups'),

    path('get/recipe/', get_recipe_view, name='get_recipe'),
    path('get/recipe_data/', get_recipe_data_view, name='get_recipe_data'),

    path('images/<slug:image_file>', recipe_image_view, name='recipe_image'),
    path('previews/<slug:image_file>', recipe_preview_view, name='recipe_image'),
]
