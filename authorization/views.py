from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.core.validators import ValidationError

from django.contrib.auth import authenticate, login, logout, get_user
from django.shortcuts import redirect

from .decorators import redirect_if_logged
from .services.db_services import *

# Create your views here.


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

        return render(request, 'login.html')

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

        return render(request, 'signup.html')

    def post(self, request, *args, **kwargs):
        next_page = request.POST.get('next')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            try:
                user = create_user_by_params(username=username, password=password)
            except ValidationError as e:
                return JsonResponse({'status': 'fail', 'message': e.message})
            login(request, user)

            return JsonResponse({'status': 'success', 'next': next_page if next_page is not None else ''})

        return JsonResponse({'status': 'fail', 'message': 'Username or password not specified'})


