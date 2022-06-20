from django.contrib.postgres.search import TrigramSimilarity
from recipes.models import Recipe


def search_for_recipe_by_title(title: str, count=10, **filters):
    return Recipe.objects.annotate(similarity=TrigramSimilarity('title', title))\
        .filter(**filters).order_by('-similarity')[:count]
