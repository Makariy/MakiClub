from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    author = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE, verbose_name='Author')

    title = models.CharField(max_length=255, null=False, verbose_name='Title')
    description = models.TextField(verbose_name='Description')

    views = models.IntegerField(null=False, default=0, verbose_name='Views count')
    groups = models.ManyToManyField('RecipeGroup', null=True, verbose_name='Group')

    image = models.FilePathField(verbose_name='Image file', null=False)
    recipe_file = models.FilePathField(verbose_name='Recipe file', null=False)
    _ingredients = models.TextField(verbose_name='Ingredients')

    date = models.TimeField(auto_now=True)

    @property
    def ingredients(self):
        return self._ingredients.split(';')

    @ingredients.setter
    def ingredients(self, value):
        self._ingredients = ';'.join(value)

    id = models.AutoField(primary_key=True, verbose_name='ID')


class RecipeGroup(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='Title')
    views = models.IntegerField(null=False, default=0, verbose_name='Views count')

    id = models.AutoField(primary_key=True, verbose_name='ID')

