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

    def test_get_last_recipes(self):
        last_recipes = get_last_recipes(count=len(self.recipes))
        self.assertEquals(last_recipes, self.recipes[::-1],
                          msg='get_last_recipes <recipes.services.db_services> returned the wrong recipes')

        exclude = self.recipes[1]
        last_recipes_with_exclude = get_last_recipes(count=len(self.recipes),
                                                     recipe_to_exclude_id=exclude.id)
        self.assertTrue(exclude not in last_recipes_with_exclude,
                        msg='get_last_recipes <recipes.services.db_services> with recipe_to_exclude_id '
                            'specified, returned the list with the recipe that had to be excluded')

        index_to_start_from = 4
        start_from = self.recipes[index_to_start_from]
        last_recipes_with_start_from = get_last_recipes(count=len(self.recipes),
                                                        recipe_to_start_id=start_from.id)
        self.assertEquals(self.recipes[:index_to_start_from][::-1], last_recipes_with_start_from)

