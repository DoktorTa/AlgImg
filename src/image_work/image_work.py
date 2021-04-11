import cv2
import numpy as np


def view_image(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_image_different_color_space(image, arg):
    return cv2.cvtColor(image, arg)


def extract_contours(image: np.ndarray, color_range) -> np.ndarray:
    """
    Поиск контуров на изображении.

    :param image: предварительно обработанное изображение с нанесенными рамками.
    :return: контуры на изображении.
    """
    # Диапазон цвета которого не может быть в документе (в нашем случае - синий)
    upper_range = np.array(color_range[0])
    lower_range = np.array(color_range[1])

    image_mask = cv2.inRange(image, lower_range, upper_range)

    contours_of_frames, _ = cv2.findContours(
        image_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    return contours_of_frames


def extract_frames(contours_of_frames: np.ndarray) -> list:
    """
    Поиск рамок на изображении.

    :param contours_of_frames: контуры на изображении.
    :return: полученные координаты рамок.
    """
    frames = []

    # перебираем все найденные контуры в цикле
    for contours_of_frame in contours_of_frames:
        rect = cv2.minAreaRect(contours_of_frame)  # пытаемся вписать прямоугольник
        box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
        box = np.int0(box)  # округление координат
        area = int(rect[1][0] * rect[1][1])  # вычисление площади

        if area > 250:
            frames.append(box[[1, 3]])

    return np.array(frames).tolist()


def search_rectangles_of_color(image_for_processing, color_range):

    contours_of_frames = extract_contours(image_for_processing, color_range)
    frames = extract_frames(contours_of_frames)

    cords = {str(i): frame for i, frame in enumerate(frames)}

    for location in frames:
        x_0 = location[0][0]
        y_0 = location[0][1]
        x_1 = location[1][0]
        y_1 = location[1][1]

        cv2.rectangle(image_for_processing, (x_0, y_0), (x_1, y_1), (0, 0, 0), 3)

    return image_for_processing, cords

