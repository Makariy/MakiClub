from datetime import datetime, timedelta

from django.shortcuts import render
from django.http.response import JsonResponse
from .services.db_services import *

# Create your views here.


def ajax_get_recipe_best_today(request):
    recipes = get_best_recipes_by_start_date(datetime.now(), 1)
    return JsonResponse({
        'recipe': {
            'title': recipes[0].title,
            'description': recipes[0].description,
            'id': recipes[0].id
        } if recipes else []
    })


def ajax_get_recipe_best_month(request):
    recipes = get_best_recipes_by_start_date(datetime.now() - timedelta(days=30), 2)
    return JsonResponse({'recipes': [{
            'title': recipe.title,
            'description': recipe.description,
            'id': recipe.id
        } for recipe in recipes]
    })

