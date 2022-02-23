from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponseBadRequest
from django.http.response import JsonResponse

from .services.db_services import search_for_recipe_by_title
from recipes.services.json_services import render_recipes


class SearchView(View):
    def get(self, request):
        return render(request, 'search.html')


def ajax_search(request):
    title = request.GET.get('title')
    if title:
        recipes = search_for_recipe_by_title(title)
        return JsonResponse(render_recipes(recipes))

    return HttpResponseBadRequest()

