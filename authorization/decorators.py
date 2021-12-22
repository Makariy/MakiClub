from django.contrib.auth import get_user

from django.urls import reverse_lazy
from django.shortcuts import redirect


def redirect_if_logged(url=None):
    """A decorator that redirects to the url if the user is already logged.
    If url is None, redirects to '/'"""
    url = reverse_lazy('home') if not url else url

    def _decorator(func):
        def _wrapper(request, *args, **kwargs):
            user = get_user(request)
            if user and not user.is_anonymous:
                return redirect(url)
            return func(request, *args, **kwargs)
        return _wrapper
    return _decorator

