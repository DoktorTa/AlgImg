from enum import Enum
from typing import List, Tuple

from threading import Thread
from pathlib import Path


import cv2

import numpy as np

from image_work.image import Image
from image_work import image_work


class ImageProcessor:
    image: Image

    color_space = {'HVS': cv2.COLOR_BGR2HSV,
                  'YCrCb': cv2.COLOR_BGR2YCrCb,
                  'XYZ': cv2.COLOR_BGR2XYZ,
                  'RGB': cv2.COLOR_BGRA2RGB,
                  'GRAY': cv2.COLOR_BGR2GRAY}

    image_color_space = {}

    def load_image(self, url: str):
        self.image = Image(url)

    @property
    def get_color_spaces(self) -> List[str]:
        return list(self.color_space.keys())

    def create_pictures_different_color_space(self, color_space_names: List[str]) -> List[Tuple[Path, str]]:
        """
        Метод создает на основе начального изображения изображения, в других цветовых пространствах.
        Метод так же проверят переданные ему цветовые названия цветовых пространств на корректность.
        :param color_space_names: Имена цветовых пространств.
        :return: Список из таплов в котором лежит путь до файла и его цветовое пространство.
        """
        path_to_new_image = []

        exists_color_space_names = self._get_only_existing_color_spaces(color_space_names)

        for name_color_space in exists_color_space_names:
            image_in_new_color_space = self._convert_image_space_color(name_color_space)
            path = self.image.save_image(image_in_new_color_space, name_color_space)

            path_to_new_image.append((path, name_color_space))

        return path_to_new_image

    def _get_only_existing_color_spaces(self, color_space_names: List[str]) -> List[str]:
        return list(set(color_space_names).intersection(set(self.color_space.keys())))

    def _convert_image_space_color(self, name_color_space) -> np.ndarray:
        color_space = self.color_space.get(name_color_space)
        new_image = image_work.get_image_different_color_space(self.image.image, color_space)

        return new_image

    def get_all_rectangles_of_color(self, name_color_space, color_rectangels):
        image_for_processing = self.image_color_space.get(name_color_space)
        image_with_frames, cords = image_work.search_rectangles_of_color(image_for_processing.copy(),  color_rectangels)
        return image_with_frames
