from django.urls import path

from .views import ajax_get_recipes_by_groups
from .views import GroupView

urlpatterns = [
    path('get/group/', ajax_get_recipes_by_groups, name='get_recipes_by_group'),
    path('group/', GroupView.as_view(), name='recipes_by_group')
]
