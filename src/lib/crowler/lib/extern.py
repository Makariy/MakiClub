import json
from typing import Dict, List

from .file_namer import *

from .recipe_data_loader import load_recipe_image, load_recipe_preview
from .models import Recipe, RecipeDescriptionItem

from .exceptions import CannotSaveRecipeToFileException


def _render_description(description: List[RecipeDescriptionItem]) -> Dict[str, List[Dict[str, str]]]:
    return {
        'data': [{"value": item.value, "type": item.type} for item in description]
    }


def _save_recipe_data(recipe: Recipe):
    path = os.path.join(DATA_SAVING_PATH, get_file_name_for_recipe_data(recipe))
    if os.path.exists(path):
        raise CannotSaveRecipeToFileException(recipe, path)
    with open(path, 'w') as f:
        f.write(json.dumps(_render_description(recipe.description)))


def _save_recipe_image(recipe: Recipe, image: bytes):
    path = os.path.join(DATA_SAVING_PATH, get_file_name_for_image(recipe))
    if os.path.exists(path):
        raise CannotSaveRecipeToFileException(recipe, path)
    with open(path, 'wb') as f:
        f.write(image)


def _save_recipe_preview(recipe: Recipe, image: bytes):
    path = os.path.join(DATA_SAVING_PATH, get_file_name_for_preview(recipe))
    if os.path.exists(path):
        raise CannotSaveRecipeToFileException(recipe, path)
    with open(path, 'wb') as f:
        f.write(image)


def save_recipe_content(recipe: Recipe):
    recipe_image = load_recipe_image(recipe)
    recipe_preview = load_recipe_preview(recipe)

    _save_recipe_data(recipe)
    _save_recipe_image(recipe, recipe_image)
    _save_recipe_preview(recipe, recipe_preview)


