from typing import List

from pydantic import BaseModel


class Image(BaseModel):
    path: str


class ColorSpaces(BaseModel):
    image: str
    color_spaces: List[str]
