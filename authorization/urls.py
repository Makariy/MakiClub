from django.urls import path

from .views import LoginView
from .views import RegistrationView
from .views import logout_view


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout')
]