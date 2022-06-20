import requests 
from bs4 import BeautifulSoup as Soup 

from typing import List

from lib.crowler.lib.models import RecipePreview
from lib.crowler.config import *


class RecipesListParser:
	def __init__(self, url):
		self.url = url

	def _make_soup(self, url) -> Soup:
		return Soup(requests.get(url).text, "html.parser")

	def _get_recipes(self, soup: Soup) -> List[Soup]:
		return soup.find_all(**{'id': lambda a: a.startswith(RECIPES_LIST_ID) if a is not None else False})

	def _get_recipe_link(self, recipe: Soup) -> str:
		return recipe.get_attribute_list('href')[0]

	def _get_recipe_preview_url(self, recipe: Soup) -> str:
		return recipe.find(**{'class': RECIPES_LIST_RECIPE_IMAGE_CLASS}).get_attribute_list('data-src')[0]

	def _get_recipe_previews_list(self, html_recipes: List[Soup]) -> List[RecipePreview]:
		return [
			RecipePreview(
				url=self._get_recipe_link(html_recipe),
				preview_url=self._get_recipe_preview_url(html_recipe),
			)
			for html_recipe in html_recipes
		]

	def get_recipe_previews_list(self) -> List[RecipePreview]:
		soup = self._make_soup(self.url)
		html_recipes = self._get_recipes(soup)
		return self._get_recipe_previews_list(html_recipes)



