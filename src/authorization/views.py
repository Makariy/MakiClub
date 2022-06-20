from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout

from .services.db_services import *


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'})


def login_view(request, *args, **kwargs):
    next_page = request.POST.get('next')
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username and password:
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'status': 'success', 'next': next_page if next_page is not None else ''})

    return JsonResponse({'status': 'fail', 'message': 'Invalid credentials'})


def signup_view(request, *args, **kwargs):
    next_page = request.POST.get('next')
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')

    if username and password and email:
        try:
            user = create_user_by_params(username=username, password=password, email=email)
        except ValidationError as e:
            return JsonResponse({'status': 'fail', 'message': e.message})

        login(request, user)

        return JsonResponse({'status': 'success', 'next': next_page if next_page is not None else ''})

    return JsonResponse({'status': 'fail', 'message': 'Username, password or email not specified'})


