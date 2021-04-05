from threading import Thread
from pathlib import Path

import cv2

import numpy as np

from image import Image
import image_work


def save_image(image, name):
    path = Path(__file__).parent.absolute().parent / (name + '.png')
    cv2.imwrite(str(path), image)


class ManagerGroupImage:
    image_original: Image

    color_space = {'HVS': cv2.COLOR_BGR2HSV,
                  'YCrCb': cv2.COLOR_BGR2YCrCb,
                  'XYZ': cv2.COLOR_BGR2XYZ,
                  'RGB': cv2.COLOR_BGRA2RGB,
                  'GRAY': cv2.COLOR_BGR2GRAY}

    image_color_space = {}

    def __init__(self, path_to_original_image: Path):
        self.image_original = Image()
        self.image_original.load_image(path_to_original_image)

    def convert_image_space_color(self, name_color_space) -> None:
        color_space = self.color_space.get(name_color_space)

        new_image = image_work.get_image_different_color_space(self.image_original.image, color_space)

        self.image_color_space.update({name_color_space: new_image})

    def get_all_rectangles_of_color(self, name_color_space, color_rectangels):
        image_for_processing = self.image_color_space.get(name_color_space)
        image_with_frames, cords = image_work.search_rectangles_of_color(image_for_processing.copy(),  color_rectangels)
        return image_with_frames

    def example(self, name_color_space: str):
        colors_range = [[[130, 255, 255], [110, 50, 50]],
                        [[255, 255, 255], [150, 50, 50]]]

        self.convert_image_space_color(name_color_space)

        save_image(self.image_color_space.get(name_color_space), name_color_space)

        inc = 0

        for color_range in colors_range:

            image_with_frames = self.get_all_rectangles_of_color(name_color_space, color_range)
            save_image(image_with_frames, name_color_space + str(inc))
            inc += 1


if __name__ == '__main__':
    manager = ManagerGroupImage(Path(r'A:\ProgrammingLanguages\InDeveloping\Python\AlgImg\test.png'))
    manager.example('XYZ')
