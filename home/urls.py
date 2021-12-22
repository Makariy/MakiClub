from django.urls import path

from .views import LoginView
from .views import RegistrationView
from .views import logout_view

from .views import ajax_get_recipe_presentation
from .views import ajax_get_recipe_popular

from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('get/presentation/', ajax_get_recipe_presentation, name='get_presentation'),
    path('get/popular/', ajax_get_recipe_popular, name='get_popular'),

    path('login/', LoginView.as_view(), name='login'),
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout')
]
