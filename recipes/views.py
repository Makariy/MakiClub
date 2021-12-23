from datetime import datetime, timedelta

from django.shortcuts import render
from django.http.response import JsonResponse

from .services.db_services import *
from .json_services import *

# Create your views here.


def ajax_get_recipe_best_today(request):
    recipes = get_best_recipes_by_start_date(datetime.now(), 1)
    rendered = render_recipe(recipes[0], include_fields=['title', 'description', 'id']) if recipes else {}
    return JsonResponse(rendered)


def ajax_get_recipe_best_month(request):
    recipes = get_best_recipes_by_start_date(datetime.now() - timedelta(days=30), 4)
    rendered = render_recipes(recipes, include_fields=['title', 'description', 'id'])
    return JsonResponse(rendered)

