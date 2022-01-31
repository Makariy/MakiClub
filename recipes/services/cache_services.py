from typing import Dict, List
from datetime import timedelta
from django.core.cache import cache
from .db_services import *
from .json_services import *
from django.conf import settings

CACHE_TIMEOUT_RECIPES_BEST_TODAY = settings.CACHE_TIMEOUT_RECIPES_BEST_TODAY
CACHE_TIMEOUT_RECIPES_BEST_MONTH = settings.CACHE_TIMEOUT_RECIPES_BEST_MONTH
CACHE_TIMEOUT_RECIPES_BEST_FEASTS = settings.CACHE_TIMEOUT_RECIPES_BEST_FEASTS


def get_or_set_recipe_best_today() -> Dict[str, str]:
    cache_name = f'{__name__}_best_today'

    rendered = cache.get(cache_name)
    if not rendered:
        recipes = get_best_recipes_by_start_date(datetime.now(), count=1)
        rendered = render_recipe(recipes[0], include_fields=['title', 'description', 'uuid']) if recipes else {}
        cache.set(cache_name, rendered, CACHE_TIMEOUT_RECIPES_BEST_TODAY)

    return rendered


def get_or_set_recipe_best_month() -> Dict[str, List[Dict[str, str]]]:
    cache_name = f'{__name__}_best_month'

    rendered = cache.get(cache_name)
    if not rendered:
        recipes = get_best_recipes_by_start_date(datetime.now() - timedelta(days=30), count=2)
        rendered = render_recipes(recipes, include_fields=['title', 'description', 'uuid'])
        cache.set(cache_name, rendered, CACHE_TIMEOUT_RECIPES_BEST_MONTH)

    return rendered


def get_or_set_recipe_best_feasts() -> Dict[str, List[Dict[str, str]]]:
    cache_name = f'{__name__}_best_feasts'

    rendered = cache.get(cache_name)
    if not rendered:
        recipes = get_best_recipes_by_start_date(datetime.now() - timedelta(days=30), count=3)
        rendered = render_recipes(recipes, include_fields=['title', 'description', 'uuid'])
        cache.set(cache_name, rendered, CACHE_TIMEOUT_RECIPES_BEST_FEASTS)
    return rendered


def get_or_set_recipe_groups() -> Dict[str, List[Dict[str, str]]]:
    cache_name = f'{__name__}_groups'

    rendered = cache.get(cache_name)
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

        cache.set(cache_name, rendered, CACHE_TIMEOUT_RECIPES_BEST_FEASTS)
    return rendered
