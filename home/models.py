from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=255, null=False, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.FilePathField(verbose_name='Image file', null=False)
    recipe_file = models.FilePathField(verbose_name='Recipe file', null=False)
    _ingredients = models.TextField(verbose_name='Ingredients')

    @property
    def ingredients(self):
        return self._ingredients.split(';')

    @ingredients.setter
    def ingredients(self, value):
        self._ingredients = ';'.join(value)

    id = models.AutoField(primary_key=True, verbose_name='ID')
