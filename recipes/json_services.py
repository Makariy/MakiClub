from .models import Recipe  # type: Ignore
from typing import Tuple, Dict  # type: Ignore
from django.db import models


def render_recipe(recipe: Recipe, include_fields=None) -> Dict[str, Dict[str, Recipe]]:
    """Returns a dict with rendered recipe <recipes.models.Recipe>,
    if include_fields is an iterable sequence, include only the fields
    specified in it, else includes all the fields of the recipe"""
    if include_fields is None:
        result = {
            'recipe': {
                'title': recipe.title,
                'author': recipe.author.username,
                'author_id': recipe.author.id,
                'image_file': recipe.image,
                'ingredients': recipe.ingredients,
                'date': recipe.date,
                'description': recipe.description,
                'id': recipe.id
            }
        }
    else:
        recipe_result = {}
        for field in include_fields:
            if '__' in field:
                tree = field.split('__')
                cls = recipe
                for obj in tree:
                    cls = getattr(cls, obj)
                recipe_result[field] = cls
            else:
                recipe_result[field] = getattr(recipe, field)
        result = {'recipe': recipe_result}

    return result


def render_recipes(recipes: Tuple[Recipe], include_fields=None) -> Dict[str, Tuple[Dict[str, Recipe]]]:
    """Returns a dict with rendered recipes <recipes.models.Recipe>,
    if include_fields is an iterable sequence, includes the fields
    specified in it, else includes all the fields of the recipe"""
    return {
        'recipes': [render_recipe(recipe, include_fields) for recipe in recipes]
    }
