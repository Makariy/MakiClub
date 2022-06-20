from typing import List

from .config import RECIPES_LIST_URL

from .lib.models import RecipePreview
from .lib.file_namer import *
from .lib.parsers.recipes_list_parser import RecipesListParser
from .lib.parsers.recipe_description_parser import RecipeDescriptionParser

from .lib.extern import save_recipe_content
from .lib.db_saver import save_recipe_to_db
from .lib.exceptions import CannotSaveRecipeToFileException, CannotParseRecipeException, RecipeWasAlreadySavedException


def get_recipe_previews_list(url) -> List[RecipePreview]:
	return RecipesListParser(url).get_recipe_previews_list()


def load_recipe_description(recipe_preview: RecipePreview) -> Recipe:
	return RecipeDescriptionParser().load_description_for_recipe(recipe_preview)


def save_recipes_from_recipe_previews(recipe_previews: List[RecipePreview]):
	for recipe_preview in recipe_previews:
		try:
			recipe = load_recipe_description(recipe_preview)
			save_recipe_to_db(recipe)
			save_recipe_content(recipe)
			print(f"Loaded recipe: {recipe.title}")
		except CannotParseRecipeException as e:
			print(e)
		except RecipeWasAlreadySavedException as e:
			print(e)
		except CannotSaveRecipeToFileException as e:
			print(e)


def start():
	recipe_previews = get_recipe_previews_list(url=RECIPES_LIST_URL)
	save_recipes_from_recipe_previews(recipe_previews)

	print('-----'*20)
	print('\t' * 4 + 'Loaded')
	print('-----'*20)
