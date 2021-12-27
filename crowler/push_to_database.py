from recipes.models import Recipe, RecipeGroup 
from recipes.services.db_services import get_recipe_group_by_params
import json 


def push_recipes_to_database(author):
	recipes_file = open('data/recipes.dat', 'r')
	recipes = json.loads(recipes_file.read())['recipes']

	for recipe in recipes:
		recipe_groups = []
		for recipe_group in recipe['filters']:
			group = get_recipe_group_by_params(title=recipe_group)
			if not group:
				group = RecipeGroup.objects.create(title=recipe_group)
			recipe_groups.append(group)

		Recipe.objects.create(
			author=author,
			title=recipe['title'],
			description=', '.join(recipe['filters']),
			image_file=recipe['preview_link'],
			recipe_file=recipe['data_file'],
			uuid=recipe['uuid'],
		).groups.add(*recipe_groups)



