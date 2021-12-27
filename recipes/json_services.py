from .models import Recipe  # type: Ignore
from typing import Dict, List, Union
from django.db import models


def render_recipe(recipe: Recipe, include_fields=None) -> Dict[str, Union[str, List[str]]]:
    """Returns a dict with rendered recipe <recipes.models.Recipe>,
    if include_fields is an iterable sequence, include only the fields
    specified in it, else includes all the fields of the recipe"""
    result = {
        'title': recipe.title,
        'author': recipe.author.username,
        'author_id': recipe.author.id,
        'image_link': recipe.image_file,
        'ingredients': recipe.ingredients,
        'date': recipe.date,
        'description': recipe.description,
        'groups': [group.title for group in recipe.groups.all()],
        'uuid': recipe.uuid
    }

    if include_fields is not None:
        for field in list(result.keys()):
            if field not in include_fields:
                result.pop(field)

    return result


def render_recipes(recipes: List[Recipe], include_fields=None) -> List[Dict[str, Dict[str, str]]]:
    """Returns a dict with rendered recipes <recipes.models.Recipe>,
    if include_fields is an iterable sequence, includes the fields
    specified in it, else includes all the fields of the recipe"""
    return [{'recipe': render_recipe(recipe, include_fields)} for recipe in recipes]

