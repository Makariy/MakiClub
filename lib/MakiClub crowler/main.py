from lib import RecipesListCrowler, RecipeDescriptionCrowler
import json 
from uuid import uuid4 
from config import *


recipes_list_url = 'https://www.simplyrecipes.com/most-recent-5121175'




def get_recipes_list(url):
	crowler = RecipesListCrowler(url)
	return crowler.get_recipes() 


def load_recipes_descriptions(recipes_list):
	for recipe in recipes_list:
		crowler = RecipeDescriptionCrowler(recipe['link'])
		uuid = uuid4()
		recipe_rendered = crowler.get_recipe_rendered()['recipe']

		file_name = f'{RECIPES_DATA_OUTPUT_PATH}/{uuid}.dat'
		with open(file_name, 'w') as file:
			file.write(json.dumps({recipe_rendered}))

		recipe['uuid'] = uuid.hex 
		recipe['data_file'] = file_name
		recipe['filters'] = recipe_rendered['filters']

	return recipes_list 


if __name__ == '__main__':
	recipes_list = get_recipes_list(recipes_list_url)
	recipes_list = load_recipes_descriptions(recipes_list)
	with open(f'{RECIPES_OUTPUT_PATH}/recipes.dat', 'w') as file:
		file.write(json.dumps({
			'recipes': recipes_list
		}))
	print('-----'*20)
	print('\t' * 4 + 'Loaded')
	print('-----'*20)
