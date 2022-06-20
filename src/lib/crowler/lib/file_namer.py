import os

from ..config import *
from .models import Recipe


def get_file_name_for_preview(recipe: Recipe) -> str:
    return os.path.join(RECIPES_PREVIEW_PATH, f'{recipe.uuid}')


def get_file_name_for_image(recipe: Recipe) -> str:
    return os.path.join(RECIPES_IMAGES_PATH, f'{recipe.uuid}')


def get_file_name_for_recipe_data(recipe: Recipe) -> str:
    return os.path.join(RECIPES_DATA_PATH, f'{recipe.uuid}')

