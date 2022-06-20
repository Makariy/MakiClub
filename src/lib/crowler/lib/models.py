from uuid import UUID
from typing import List, Literal, Any
from dataclasses import dataclass


@dataclass
class RecipeDescriptionItem:
    value: Any
    type: Literal['title', 'text', 'image']


@dataclass
class Recipe:
    title: str
    description: List[RecipeDescriptionItem]
    filters: List[str]
    image_url: str
    preview_url: str
    real_url: str
    uuid: UUID


@dataclass
class RecipePreview:
    url: str
    preview_url: str

