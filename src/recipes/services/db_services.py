from typing import Union, Optional

from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from recipes.models import Recipe, RecipeGroup


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
    returns the best recipes for the closest date before."""
    recipes = Recipe.objects.filter(date__gt=date).order_by('-id')

    if not recipes:
        recipes = Recipe.objects.order_by('-id')

    if groups is not None:
        if hasattr(groups, '__iter__'):
            recipes = recipes.filter(groups__in=groups)
        else:
            recipes = recipes.filter(groups=groups)

    return recipes[:count]


def order_recipe_groups_by_params(ordering, count=3):
    """Returns an ordered QuerySet with recipes groups"""
    return RecipeGroup.objects.order_by(ordering)[:count]


def get_recipes_by_group(group: RecipeGroup, count=10, date: Optional[datetime] = None):
    """Returns recipes that match the specified group with a limit of count and starting from date <date>"""
    date = date if date else datetime.now()
    return get_best_recipes_by_start_date(date, groups=[group], count=count)


def create_recipe_group(title: str) -> RecipeGroup | None:
    """Creates and returns RecipeGroup with specified title, if it already exists, returns None"""
    try:
        return RecipeGroup.objects.create(title=title)
    except IntegrityError:
        return None

