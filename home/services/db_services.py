from django.core.exceptions import ObjectDoesNotExist

from home.models import Recipe


def get_recipes(count=20, offset=0, exclude_id=None):
    if exclude_id:
        result = Recipe.objects.exlcude(id=exclude_id)
    else:
        result = Recipe.objects.all()

    return result[offset:offset+count]
