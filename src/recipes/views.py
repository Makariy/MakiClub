import os

from django.conf import settings
from django.http.response import JsonResponse, HttpResponseBadRequest, FileResponse

from .services.remote_services import get_recipe_data
from .services.cache_services import *

from lib.utils.type_converter import convert_string_to_uuid


CACHE_TIMEOUT_RECIPES_BEST_TODAY = settings.CACHE_TIMEOUT_RECIPES_BEST_TODAY
CACHE_TIMEOUT_RECIPES_BEST_MONTH = settings.CACHE_TIMEOUT_RECIPES_BEST_MONTH
CACHE_TIMEOUT_RECIPES_BEST_FEASTS = settings.CACHE_TIMEOUT_RECIPES_BEST_FEASTS


# Just for some time
def recipe_image_view(request, image_file):
    path = f'data/images/{image_file}'
    if os.path.exists(path):
        headers = {
            'Cache-Control': 'max-age=36000'
        }
        return FileResponse(open(path, 'rb'),
                            content_type='image/png',
                            headers=headers)
    else:
        return HttpResponseBadRequest()


# Just for some time
def recipe_preview_view(request, image_file):
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


def get_recipe_best_today_view(request):
    rendered = get_or_set_recipe_best_today_cached()
    return JsonResponse(rendered)


def get_recipe_best_month_view(request):
    rendered = get_or_set_recipe_best_month_cached()
    return JsonResponse(rendered)


def get_best_feasts_view(request):
    rendered = get_or_set_recipe_best_feasts_cached()
    return JsonResponse(rendered)


def get_groups_view(request):
    rendered = get_or_set_recipe_groups_cached()
    return JsonResponse(rendered)


def get_recipe_data_view(request):
    recipe_uuid = request.GET.get('recipe_uuid')
    if not recipe_uuid:
        return JsonResponse({
            'status': 'fail',
            'error': 'recipe_uuid is not specified'
        })

    recipe_uuid = convert_string_to_uuid(recipe_uuid)
    if not recipe_uuid:
        return JsonResponse({
            'status': 'fail',
            'error': 'recipe_uuid is not a valid UUID'
        })

    recipe = get_recipe_by_params(uuid=recipe_uuid)
    if not recipe:
        return JsonResponse({
            'status': 'fail',
            'error': 'recipe with this UUID does not exist'
        })

    data = get_recipe_data(recipe)
    return JsonResponse(data)


def get_recipe_view(request):
    recipe_uuid = request.GET.get('recipe_uuid')
    if not recipe_uuid:
        return JsonResponse({
            'status': 'fail',
            'error': 'recipe_uuid is not specified'
        })

    recipe_uuid = convert_string_to_uuid(recipe_uuid)
    if not recipe_uuid:
        return JsonResponse({
            'status': 'fail',
            'error': 'recipe_uuid is not a valid uuid'
        })

    recipe = get_recipe_by_params(uuid=recipe_uuid)
    if not recipe:
        return JsonResponse({
            'status': 'fail',
            'error': 'recipe_with this uuid does not exist'
        })

    return JsonResponse({
        **render_recipe(recipe),
        'status': 'success'
    })

