from typing import Union

from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from recipes.models import Recipe, RecipeGroup
from uuid import UUID


def convert_string_to_uuid(uuid: str) -> UUID:
    """Converts uuid of type str to UUID. If param is not valid, returns None"""
    try:
        return UUID(uuid)
    except ValueError:
        return None


def get_recipe_by_params(**params) -> Union[Recipe, None]:
    """Returns the recipe that suites the params. If the recipe does not exist, returns None"""
    try:
        return Recipe.objects.get(**params)
    except ObjectDoesNotExist:
        return None


def get_recipe_group_by_params(**params):
    """Returns a recipe group that suites the params. If the group does not exist, returns None"""
    try:
        return RecipeGroup.objects.get(**params)
    except ObjectDoesNotExist:
        return None


def get_best_recipes_by_start_date(date: datetime, groups=None, count=10):
    """Returns the best recipes for the specified date with groups <groups>, if there is no recipes for that date,
    returns the best recipes for the most closest date before."""
    recipes = Recipe.objects.filter(date__gt=date).order_by('-id')
    if not recipes:
        recipes = Recipe.objects.order_by('-id')

    if groups is not None:
        recipes = recipes.filter(groups=groups)

    return recipes[:count]


def order_recipe_groups_by_params(ordering, count=3):
    """Returns an ordered QuerySet with recipes groups"""
    return RecipeGroup.objects.order_by(ordering)[:count]


