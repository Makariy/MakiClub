import requests 
from bs4 import BeautifulSoup as Soup 

from typing import Tuple, Dict, List  

from config import * 



class RecipesListCrowler:
	def __init__(self, url):
		self.url = url

	def _get_recipes(self, soup: Soup) -> List[Soup]:
		return soup.find(id=RECIPES_LIST_ID).find_all(**{'class': RECIPES_LIST_RECIPE_CLASS})

	def _get_recipe_title(self, recipe: Soup) -> str:
		return recipe.find(**{'class': RECIPES_LIST_RECIPE_TITLE_CLASS}).text.replace('\n', '')

	def _get_recipe_link(self, recipe: Soup) -> str:
		return recipe.find(**{'class': RECIPES_LIST_RECIPE_LINK_CLASS}).get_attribute_list('href')[0]

	def _get_recipe_preview_link(self, recipe: Soup) -> str:
		return recipe.find(**{'class': RECIPES_LIST_RECIPE_IMAGE_CLASS}).get_attribute_list('data-src')[0]

	def _make_soup(self, url) -> Soup:
		return Soup(requests.get(url).text)

	def render_recipe(self, recipe: Soup) -> Dict[str, str]:
		return {
			'title': self._get_recipe_title(recipe),
			'link': self._get_recipe_link(recipe),
			'preview_link': self._get_recipe_preview_link(recipe),
		}

	def render_recipes(self, recipes: List[Soup]) -> Dict[str, List[Dict[str, str]]]:
		return [self.render_recipe(recipe) for recipe in recipes]

	def get_recipes(self):
		soup = self._make_soup(self.url)
		recipes = self._get_recipes(soup)
		return self.render_recipes(recipes)


