from django.shortcuts import render
from django.http import JsonResponse

from django.views import View

from .services.db_services import *


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

