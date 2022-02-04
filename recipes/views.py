import os

from django.shortcuts import render
from django.views.generic import View
from django.http.response import JsonResponse, HttpResponseBadRequest, FileResponse
from django.conf import settings

from .services.db_services import *
from .services.remote_services import get_recipe_data
from .services.json_services import *
from .services.cache_services import *

CACHE_TIMEOUT_RECIPES_BEST_TODAY = settings.CACHE_TIMEOUT_RECIPES_BEST_TODAY or 3600
CACHE_TIMEOUT_RECIPES_BEST_MONTH = settings.CACHE_TIMEOUT_RECIPES_BEST_MONTH or 3600 * 30
CACHE_TIMEOUT_RECIPES_BEST_FEASTS = settings.CACHE_TIMEOUT_RECIPES_BEST_FEASTS or 3600 * 3


class RecipeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'recipe.html')


# Just for some time
def recipe_image_view(request, image_file):
    path = f'data/previews/{image_file}'
    if os.path.exists(path):
        headers = {
            'Cache-Control': 'max-age=36000'
        }
        return FileResponse(open(path, 'rb'),
                            content_type='image/png',
                            headers=headers)
    else:
        return HttpResponseBadRequest()


def ajax_get_recipe_best_today(request):
    rendered = get_or_set_recipe_best_today()
    return JsonResponse(rendered)


def ajax_get_recipe_best_month(request):
    rendered = get_or_set_recipe_best_month()
    return JsonResponse(rendered)


def ajax_get_best_feasts(request):
    rendered = get_or_set_recipe_best_feasts()
    return JsonResponse(rendered)


def ajax_get_groups(request):
    rendered = get_or_set_recipe_groups()
    return JsonResponse(rendered)


def ajax_get_recipe_data(request):
    recipe_uuid = convert_string_to_uuid(request.GET.get('recipe_uuid'))
    if recipe_uuid:
        recipe = get_recipe_by_params(uuid=recipe_uuid)
        data = get_recipe_data(recipe)
        return JsonResponse(data)
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


