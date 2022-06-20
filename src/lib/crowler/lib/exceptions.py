from .models import Recipe


class CannotSaveRecipeToFileException(Exception):
    def __init__(self, recipe: Recipe, path, *args):
        self.recipe = recipe
        self.path = path
        super().__init__(*args)

    def __str__(self):
        return f"Cannot save recipe: {self.recipe} to file: {self.path}"


class CannotParseRecipeException(Exception):
    def __init__(self, url: str, *args):
        self.url = url
        super().__init__(*args)

    def __str__(self):
        return f"Cannot parse recipe: {self.url}"


class RecipeWasAlreadySavedException(Exception):
    def __init__(self, recipe: Recipe, *args):
        self.recipe = recipe
        super().__init__(*args)

    def __str__(self):
        return f"Recipe '{self.recipe.title}' was already saved"
