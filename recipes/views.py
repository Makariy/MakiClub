from datetime import datetime, timedelta

from django.shortcuts import render
from django.views.generic import View
from django.http.response import JsonResponse, FileResponse, HttpResponseBadRequest
from django.core.cache import cache
from django.conf import settings

from .services.db_services import *
from .json_services import *

import json


# Create your views here.


CACHE_TIMEOUT_RECIPES_BEST_TODAY = settings.CACHE_TIMEOUT_RECIPES_BEST_TODAY
CACHE_TIMEOUT_RECIPES_BEST_MONTH = settings.CACHE_TIMEOUT_RECIPES_BEST_MONTH
CACHE_TIMEOUT_RECIPES_BEST_FEASTS = settings.CACHE_TIMEOUT_RECIPES_BEST_FEASTS


class RecipeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'recipe.html')


def ajax_get_recipe_best_today(request):
    rendered = cache.get(f'{__name__}_best_today')
    if not rendered:
        recipes = get_best_recipes_by_start_date(datetime.now(), count=1)
        rendered = {
            'recipe': render_recipe(recipes[0], include_fields=['title', 'description', 'uuid']) if recipes else {}
        }
        cache.set(f'{__name__}_best_today', rendered, CACHE_TIMEOUT_RECIPES_BEST_TODAY)

    return JsonResponse(rendered)


def ajax_get_recipe_best_month(request):
    rendered = cache.get(f'{__name__}_best_month')
    if not rendered:
        recipes = get_best_recipes_by_start_date(datetime.now() - timedelta(days=30), count=2)
        rendered = {
            'recipes': render_recipes(recipes, include_fields=['title', 'description', 'uuid'])
        }

        cache.set(f'{__name__}_best_month', rendered, CACHE_TIMEOUT_RECIPES_BEST_MONTH)
    return JsonResponse(rendered)


def ajax_get_best_feasts(request):
    rendered = cache.get(f'{__name__}_best_feasts')
    if not rendered:
        recipes = get_best_recipes_by_start_date(datetime.now() - timedelta(days=30), count=3)
        rendered = {
            'recipes': render_recipes(recipes, include_fields=['title', 'description', 'uuid'])
        }
        cache.set(f'{__name__}_best_feasts', rendered, CACHE_TIMEOUT_RECIPES_BEST_FEASTS)
    return JsonResponse(rendered)


def ajax_get_groups(request):
    rendered = cache.get(f'{__name__}_groups')
    if not rendered:
        rendered = {
            'groups': []
        }
        best_groups = order_recipe_groups_by_params('-id', 3)
        for group in best_groups:
            recipes = get_best_recipes_by_start_date(datetime.now(), count=3, groups=group)
            rendered['groups'].append({
                'title': group.title,
                'recipes': render_recipes(recipes)
            })

        cache.set(f'{__name__}_groups', rendered, CACHE_TIMEOUT_RECIPES_BEST_FEASTS)
    return JsonResponse(rendered)


def ajax_get_recipe_data(request):
    recipe_uuid = convert_string_to_uuid(request.GET.get('recipe_uuid'))
    if recipe_uuid:
        recipe = get_recipe_by_params(uuid=recipe_uuid)
        recipe_file = open(f'data/{recipe.recipe_file}', 'r')
        return JsonResponse(json.loads(recipe_file.read()))
    return HttpResponseBadRequest()


def ajax_get_recipe(request):
    recipe_uuid = convert_string_to_uuid(request.GET.get('recipe_uuid'))
    if recipe_uuid:
        recipe = get_recipe_by_params(uuid=recipe_uuid)

        return JsonResponse({
            'recipe': render_recipe(recipe),
            'status': 'success'
        })

    return JsonResponse({
        'status': 'fail'
    })


