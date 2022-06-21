from django.http.response import JsonResponse

from .services.cache_services import *

from lib.utils.type_converter import convert_string_to_uuid


CACHE_TIMEOUT_RECIPES_BEST_TODAY = settings.CACHE_TIMEOUT_RECIPES_BEST_TODAY
CACHE_TIMEOUT_RECIPES_BEST_MONTH = settings.CACHE_TIMEOUT_RECIPES_BEST_MONTH
CACHE_TIMEOUT_RECIPES_BEST_FEASTS = settings.CACHE_TIMEOUT_RECIPES_BEST_FEASTS


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

