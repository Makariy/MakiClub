from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist

from recipes.models import Recipe, RecipeGroup


def get_last_recipes(count=20, recipe_to_start_id=None, recipe_to_exclude_id=None):
    """Returns the last <count> recipes. If the <recipe_to_start_id> is not None,
    returns all the recipes that had been published before the recipe with id <recipe_to_start_id>.
    And if <recipe_to_exclude_id> is not None, excludes the recipe with this id"""
    if recipe_to_exclude_id is not None:
        result = Recipe.objects.all().exclude(id=recipe_to_exclude_id)
    else:
        result = Recipe.objects.all()

    if recipe_to_start_id is not None:
        result = result.filter(id__lt=recipe_to_start_id)

    return result[:count:-1]


def get_recipe_by_params(**params):
    """Returns the recipe that suites the params. If the recipe does not exist, returns None"""
    try:
        return Recipe.objects.get(**params)
    except ObjectDoesNotExist:
        return None


def get_best_recipes_by_start_date(date: datetime, count=10, **other):
    """Returns the best recipes for the specified date, if there is no recipes for that date,
    returns the best recipes for the most closest date before."""
    recipes = Recipe.objects.filter(date__gt=date).filter(**other).order_by('-id')[:count]

    if not recipes:
        recipes = Recipe.objects.order_by('-id').filter(**other)[:count]

    return recipes


def order_recipe_groups_by_params(ordering):
    """Returns an ordered QuerySet with recipes groups"""
    return RecipeGroup.objects.order_by(ordering)
