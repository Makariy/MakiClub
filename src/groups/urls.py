from django.urls import path

from .views import get_recipes_by_groups_view

urlpatterns = [
    path('get/group/', get_recipes_by_groups_view, name='get_recipes_by_group'),
]
