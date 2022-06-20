from .file_namer import *

from django.contrib.auth.models import User
from recipes.models import Recipe as DBRecipe
from recipes.services.db_services import get_recipe_by_params, get_recipe_group_by_params, create_recipe_group

from .models import Recipe
from .exceptions import RecipeWasAlreadySavedException


def set_groups_for_recipe(db_recipe: DBRecipe, recipe: Recipe):
	groups = []
	for filter in recipe.filters:
		group = get_recipe_group_by_params(title=filter)
		if not group:
			group = create_recipe_group(title=filter)
		groups.append(group)
	db_recipe.groups.set(groups)


def save_recipe_to_db(recipe: Recipe):
	if get_recipe_by_params(real_url=recipe.real_url) is not None:
		raise RecipeWasAlreadySavedException(recipe)
	db_recipe = DBRecipe.objects.create(
		author=User.objects.first(),
		title=recipe.title,
		description=', '.join(recipe.filters),
		recipe_file=get_file_name_for_recipe_data(recipe),
		image_file=get_file_name_for_image(recipe),
		preview_file=get_file_name_for_preview(recipe),
		_ingredients=['NOTHING'],
		real_url=recipe.real_url,
		uuid=recipe.uuid
	)
	set_groups_for_recipe(db_recipe, recipe)
	return db_recipe

