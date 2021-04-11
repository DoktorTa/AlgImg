import os
from pathlib import Path

import cv2
import numpy as np

from image_work import *


class Image:
    image: np.ndarray

    def __init__(self, url: str):
        if self._checking_if_there_is_file_in_the_fs(url):
            path = self._generate_path(url)
            self.load_image(path)

    def _checking_if_there_is_file_in_the_fs(self, url: str) -> bool:
        return Path.exists(self._generate_path(url))

    @staticmethod
    def _generate_path(suffix_path: str) -> Path:
        return Path(__file__).parent.absolute().parent.parent / suffix_path

    def load_image(self, path: Path):
        self.image = cv2.imread(str(path))

    @staticmethod
    def save_image(image, name) -> Path:
        path = Path(__file__).parent.absolute().parent.parent / (name + '.png')
        cv2.imwrite(str(path), image)
        return path
