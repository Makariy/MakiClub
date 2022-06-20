from recipes.models import Recipe, RecipeGroup  # types
from typing import Dict, List, Union, Literal


def render_recipe_group(group: RecipeGroup, include_fields=None) \
        -> Dict[Literal['group'], Dict[str, Union[str, List[str]]]]:
    result = {
        'title': group.title,
        'uuid': group.uuid
    }
    if include_fields is not None:
        for field in list(result.keys()):
            if field not in include_fields:
                result.pop(field)

    return {
        'group': result
    }


def render_recipe_groups(groups: List[RecipeGroup], include_fields=None) \
        -> Dict[Literal['groups'], List[Dict[str, Dict[str, Union[str, List[str]]]]]]:
    return {
        'groups': [render_recipe_group(group, include_fields=include_fields) for group in groups]
    }


def render_recipe(recipe: Recipe, include_fields=None) \
        -> Dict[Literal['recipe'], Dict[str, Union[str, List[str]]]]:
    """Returns a dict with rendered recipe <recipes.models.Recipe>,
    if include_fields is an iterable sequence, include only the fields
    specified in it, else includes all the fields of the recipe"""
    result = {
        'title': recipe.title,
        'author': recipe.author.username,
        'author_id': recipe.author.id,
        'image_url': recipe.image_file,
        'preview_url': recipe.preview_file,
        'ingredients': recipe.ingredients,
        'date': recipe.date,
        'description': recipe.description,
        'groups': [render_recipe_group(group) for group in recipe.groups.all()],
        'uuid': recipe.uuid
    }

    if include_fields is not None:
        for field in list(result.keys()):
            if field not in include_fields:
                result.pop(field)

    return {
        'recipe': result
    }


def render_recipes(recipes: List[Recipe], include_fields=None)\
        -> Dict[Literal['recipes'], List[Dict[str, Dict[str, Union[str, List[str]]]]]]:
    """Returns a dict with rendered recipes <recipes.models.Recipe>,
    if include_fields is an iterable sequence, includes the fields
    specified in it, else includes all the fields of the recipe"""
    return {
        'recipes': [render_recipe(recipe, include_fields=include_fields) for recipe in recipes]
    }
