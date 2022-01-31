from django.test import TestCase
from django.contrib.auth.models import User

from .models import Recipe
from .services.db_services import *

# Create your tests here.


class GetRecipesTests(TestCase):
    def setUp(self):
        self.recipes = []
        self.user = User.objects.create_user(username='TestUser', password='TestUserPassword123')
        for i in range(10):
            self.recipes.append(Recipe.objects.create(
                title=f'Test recipe {i}',
                description=f'Test recipe description {i}',
                recipe_file=f'Test recipe file {i}',
                ingredients=['Ingredient 1', 'Ingredient 2']
            ))

    def test_get_recipe_by_params(self):
        recipe = self.recipes[0]
        self.assertEquals(recipe, get_recipe_by_params(id=recipe.id),
                          msg='get_recipe_by_params <recipes.services.db_services> returned the wrong recipe')
        self.assertEquals(None, get_recipe_by_params(title=""),
                          msg='get_recipe_by_params <recipes.services.db_services> returned the wrong recipe')

