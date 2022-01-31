import json
from typing import Dict, List, Any
from recipes.models import Recipe, RecipeGroup  # type


def get_recipe_data(recipe: Recipe) -> Dict[str, Any]:
    with open('data/' + recipe.recipe_file, 'r') as file:
        return json.loads(file.read())
