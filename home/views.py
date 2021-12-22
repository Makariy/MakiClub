from django.shortcuts import render
from django.http import JsonResponse

from django.views import View

from .services.db_services import *


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/home.html')


def ajax_get_recipe_presentation(request):
    recipes = get_recipes(count=5)
    return JsonResponse({
        'recipes': [{
            'title': recipe.title,
            'description': recipe.description,
            'id': recipe.id
        } for recipe in recipes]
    })


def ajax_get_recipe_popular(request):
    recipes = get_recipes(count=15)
    return JsonResponse({'popular': [{'id': recipe.id} for recipe in recipes]})
