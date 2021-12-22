from django.contrib.auth import authenticate, login, logout, get_user

from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.core.validators import ValidationError
from django.utils.decorators import method_decorator

from django.views import View
from django.shortcuts import redirect


from .validators import UserValidator
from authorization.services.db_services import *
from .services.db_services import *

from authorization.decorators import redirect_if_logged


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'})


@method_decorator(redirect_if_logged(), 'dispatch')
class LoginView(View):
    def get(self, request, *args, **kwargs):
        next_page = request.GET.get('next')
        if next_page is None:
            next_page = ''

        user = get_user(request)
        if user and not user.is_anonymous:
            return redirect(next_page)

        return render(request, 'main/login.html')

    def post(self, request, *args, **kwargs):
        next_page = request.POST.get('next')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({'status': 'success', 'next': next_page if next_page is not None else ''})

        return JsonResponse({'status': 'fail', 'message': 'Invalid credentials'})


@method_decorator(redirect_if_logged(), 'dispatch')
class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        next_page = request.GET.get('next')
        if next_page is None:
            next_page = ''

        user = get_user(request)
        if user and not user.is_anonymous:
            return redirect(next_page)

        return render(request, 'main/signup.html')

    def post(self, request, *args, **kwargs):
        next_page = request.POST.get('next')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = User(username=username, password=password)
            try:
                UserValidator.validate(user)
            except ValidationError as e:
                return JsonResponse({'status': 'fail', 'message': e.message})
            create_user_by_params(username=username, password=password)
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return JsonResponse({'status': 'success', 'next': next_page if next_page is not None else ''})

        return JsonResponse({'status': 'fail', 'message': 'Username or password not specified'})


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
