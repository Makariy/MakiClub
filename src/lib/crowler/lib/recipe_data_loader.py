from .models import Recipe  # type
import requests


def load_recipe_image(recipe: Recipe) -> bytes:
    return requests.get(recipe.image_url).content


def load_recipe_preview(recipe: Recipe) -> bytes:
    return requests.get(recipe.preview_url).content


