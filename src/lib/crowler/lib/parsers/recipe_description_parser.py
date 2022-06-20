import requests
from uuid import uuid4
from bs4 import BeautifulSoup as Soup
from typing import List

from lib.crowler.lib.models import Recipe, RecipeDescriptionItem, RecipePreview
from lib.crowler.config import *
from ..exceptions import CannotParseRecipeException


RECIPE_TITLE_CLASS = 'heading__title'
RECIPE_IMAGE_CLASS = 'mntl-primary-image'
RECIPE_DESCRIPTION_ELEMENT_CLASS = 'mntl-sc-block'

RECIPE_DESCRIPTION_ELEMENT_TITLE_CLASS = 'mntl-sc-block-heading__text'
RECIPE_DESCRIPTION_ELEMENT_TEXT_CLASS = 'mntl-sc-block-html'
RECIPE_DESCRIPTION_ELEMENT_IMAGE_CLASS = 'mntl-sc-block-image'


class StepsDumper:
	@staticmethod
	def _dump_title(step: Soup) -> RecipeDescriptionItem:
		title = step.find(**{'class': RECIPE_DESCRIPTION_ELEMENT_TITLE_CLASS}).text
		return RecipeDescriptionItem(value=title, type='title')

	@staticmethod
	def _dump_text(step: Soup) -> RecipeDescriptionItem:
		return RecipeDescriptionItem(value=step.text, type='text')

	@staticmethod
	def _dump_image(step: Soup) -> RecipeDescriptionItem:
		tag = step.find('img')
		image_link = tag.get_attribute_list('data-src')[0]
		return RecipeDescriptionItem(value=image_link, type='image')

	@staticmethod 
	def dump(step: Soup) -> RecipeDescriptionItem:
		classes = step.get_attribute_list('class')
		if RECIPE_DESCRIPTION_ELEMENT_TITLE_CLASS in classes:
			return StepsDumper._dump_title(step)
		elif RECIPE_DESCRIPTION_ELEMENT_TEXT_CLASS in classes:
			return StepsDumper._dump_text(step)
		elif RECIPE_DESCRIPTION_ELEMENT_IMAGE_CLASS in classes:
			return StepsDumper._dump_image(step)


class RecipeDescriptionParser:
	def _make_soup(self, url):
		return Soup(requests.get(url).text, "html.parser")

	def _get_all_steps(self, soup: Soup) -> List[Soup]:
		return soup.find_all(**{'class': RECIPE_DESCRIPTION_ELEMENT_CLASS})

	def _get_title(self, soup: Soup) -> str:
		return soup.find(**{'class': RECIPE_TITLE_CLASS}).text

	def _get_image_url(self, soup: Soup) -> str:
		return soup.find(**{'class': RECIPE_IMAGE_CLASS}).get_attribute_list('src')[0]

	def _get_filters(self, soup: Soup) -> List[str]:
		return list(map(lambda a: a.text, 
			soup.find_all(**{'class': RECIPE_DESCRIPTION_FILTER_CLASS})))

	def render_step(self, step: Soup) -> RecipeDescriptionItem:
		return StepsDumper.dump(step)

	def render_steps(self, steps: List[Soup]) -> List[RecipeDescriptionItem]:
		return list(filter(lambda step: step is not None,
				[self.render_step(step) for step in steps]))

	def load_description_for_recipe(self, recipe_preview: RecipePreview) -> Recipe:
		soup = self._make_soup(recipe_preview.url)

		try:
			return Recipe(
				title=self._get_title(soup),
				description=self.render_steps(self._get_all_steps(soup)),
				filters=self._get_filters(soup),
				image_url=self._get_image_url(soup),
				preview_url=recipe_preview.preview_url,
				uuid=uuid4(),

				real_url=recipe_preview.url,
			)
		except Exception:
			raise CannotParseRecipeException(recipe_preview.url)
