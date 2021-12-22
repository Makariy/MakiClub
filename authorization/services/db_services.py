from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def get_user_by_params(**params):
    """Returns the user that suites the params"""
    try:
        user = User.objects.get(**params)
        return user
    except ObjectDoesNotExist:
        return None


def create_user_by_params(**params):
    """Creates the user by params"""
    return User.objects.create_user(**params)


def get_all_users():
    """Returns all the users"""
    return User.objects.all()

