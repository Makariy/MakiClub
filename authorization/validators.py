from django.contrib.auth.models import User
from django.core.validators import ValidationError

# Django's user validators


def user_validate_username(user: User):
    if 1 < len(user.username) < 20 and not user.username[0].isdigit():
        return True
    raise ValidationError(message="Username is empty, too long or start's with digit")


def user_validate_username_unique(user: User):
    if User.objects.filter(username=user.username).count() == 0:
        return True
    raise ValidationError(message="User with this name already exists")


def user_validate_password(user: User):
    if 5 < len(user.password) < 36:
        return True
    raise ValidationError(message="Password's length must be greater than 5 and less than 36")


class UserValidator:
    _validators = [
        user_validate_username,
        user_validate_username_unique,
        user_validate_password,
    ]

    @staticmethod
    def validate(user: User):
        for validator in UserValidator._validators:
            validator(user)
