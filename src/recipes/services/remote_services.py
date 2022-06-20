import json
from typing import Dict, Any
from recipes.models import Recipe  # type


def get_recipe_data(recipe: Recipe) -> Dict[str, Any]:
    with open('data/' + recipe.recipe_file, 'r') as file:
        return json.loads(file.read())
