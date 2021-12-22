from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import ValidationError

from authorization.validators import UserValidator


def get_user_by_params(**params):
    """Returns the user that suites the params"""
    try:
        user = User.objects.get(**params)
        return user
    except ObjectDoesNotExist:
        return None


def create_user_by_params(**params):
    """Creates the user by params"""
    username = params.get('username')
    password = params.get('password')

    if username and password:
        user = User(username=username, password=password)
        UserValidator.validate(user)
        return User.objects.create_user(**params)
    else:
        raise ValidationError(message='Username or password not specified')


def get_all_users():
    """Returns all the users"""
    return User.objects.all()

