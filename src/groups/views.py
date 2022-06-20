from django.shortcuts import render

from django.views import View

from django.http.response import JsonResponse
from django.http.response import HttpResponseForbidden

from recipes.services.db_services import *
from recipes.services.json_services import *

from lib.utils.type_converter import convert_string_to_uuid


def get_recipes_by_groups_view(request):
    group_uuid = request.GET.get('group_uuid')
    if not group_uuid:
        return JsonResponse({
            'status': 'fail',
            'error': 'group_uuid is not specified'
        })

    group_uuid = convert_string_to_uuid(group_uuid)
    if not group_uuid:
        return JsonResponse({
            'status': 'fail',
            'error': 'group_uuid is not a valid UUID'
        })

    group = get_recipe_group_by_params(uuid=group_uuid)
    if not group:
        return JsonResponse({
            'status': 'fail',
            'error': 'group with this uuid does not exist'
        })

    recipes = get_recipes_by_group(group=group)
    rendered = {
        **render_recipes(recipes),
        **render_recipe_group(group)
    }
    return JsonResponse(rendered)


