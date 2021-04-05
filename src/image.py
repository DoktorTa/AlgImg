from pathlib import Path

import cv2
import numpy as np

from image_work import *


class Image:
    image: np.ndarray

    def load_image(self, path: Path):
        self.image = cv2.imread(str(path))
