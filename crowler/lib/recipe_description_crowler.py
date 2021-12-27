from bs4 import BeautifulSoup as Soup
import requests 
from typing import List, Dict 

from config import * 



RECIPE_DESCRIPTION_ELEMENT_CLASS = 'mntl-sc-block'
RECIPE_DESCRIPTION_ELEMENT_TITLE_CLASS = 'mntl-sc-block-heading'
RECIPE_DESCRIPTION_ELEMENT_HTML_CLASS = 'mntl-sc-block-html'
RECIPE_DESCRIPTION_ELEMENT_IMAGE_CLASS = 'mntl-sc-block-image'



class RecipeDescriptionBase: 
	def __init__(self, value):
		self.value = value 

class RecipeDescriptionTitle(RecipeDescriptionBase):
	pass 

class RecipeDescriptionHTML(RecipeDescriptionBase):
	pass 

class RecipeDescriptionImage(RecipeDescriptionBase):
	pass 



RECIPE_DESCRIPTIONS = {
	RECIPE_DESCRIPTION_ELEMENT_TITLE_CLASS: RecipeDescriptionTitle,
	RECIPE_DESCRIPTION_ELEMENT_HTML_CLASS:  RecipeDescriptionHTML,
	RECIPE_DESCRIPTION_ELEMENT_IMAGE_CLASS: RecipeDescriptionImage,
}


class DescriptionDumper:
	@staticmethod
	def _dump_title(description: RecipeDescriptionTitle) -> Dict[str, str]:
		title = description.value.find(**{'class': RECIPE_DESCRIPTION_ELEMENT_TITLE_TEXT_CLASS}).text

		return {
			'title': title,
			'type': 'title',
		}
	
	@staticmethod
	def _dump_html(description: RecipeDescriptionHTML) -> Dict[str, str]:
		return {
			'text': description.value.text,
			'type': 'text'
		}
	
	@staticmethod
	def _dump_image(description: RecipeDescriptionImage) -> Dict[str, str]:
		tag = description.value.find('img')
		image_link = tag.get_attribute_list('data-src')[0]
		return {
			'image_link': image_link,
			'type': 'image'
		}


	@staticmethod 
	def dump(description: RecipeDescriptionBase) -> Dict[str, str]:
		if isinstance(description, RecipeDescriptionTitle):
			return DescriptionDumper._dump_title(description)
		elif isinstance(description, RecipeDescriptionHTML):
			return DescriptionDumper._dump_html(description)
		elif isinstance(description, RecipeDescriptionImage):
			return DescriptionDumper._dump_image(description)


class RecipeDescriptionCrowler:
	def __init__(self, url):
		self.url = url 

	def _get_all_elements(self, soup: Soup) -> List[Soup]:
		return soup.find_all(**{'class': RECIPE_DESCRIPTION_ELEMENT_CLASS})

	def _convert_element_to_description(self, element: Soup) -> RecipeDescriptionBase:
		tags = element.get_attribute_list('class')
		for tag in tags:
			if f'{RECIPE_DESCRIPTION_ELEMENT_CLASS}-' in tag:
				description = RECIPE_DESCRIPTIONS.get(tag)
				if description:
					return description(element)

	def _get_filters(self, soup: Soup) -> List[str]:
		return list(map(lambda a: a.text, 
			soup.find_all(**{'class': RECIPE_DESCRIPTION_FILTER_CLASS})))


	def _make_soup(self, url):
		return Soup(requests.get(url).text)

	def render_element(self, element: Soup) -> Dict[str, str]:
		description = self._convert_element_to_description(element)
		if description:
			try:
				return DescriptionDumper.dump(description)
			except:
				pass 

		return None 

	def render_elements(self, elements: Soup) -> List[Dict[str, str]]:
		return list(filter(lambda element: element is not None, 
				[self.render_element(element) for element in elements]))

	def get_recipe_rendered(self) -> List[Dict[str, Dict[str, str]]]:
		soup = self._make_soup(self.url)
		elements = self._get_all_elements(soup)
		filters = self._get_filters(soup)
		return {
			'recipe': {
				'data': self.render_elements(elements),
				'filters': filters 
			}
		}
