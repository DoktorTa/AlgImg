# from image_work.image import Image
# import numpy as np
# import random as rd
# import cv2 as cv
#
#
# def alg(image: np.ndarray):
#
#     for line in image:
#
#         for px in line:
#
#             px[0] = rd.randint(0, px[0])
#             px[1] = rd.randint(0, px[1])
#             px[2] = rd.randint(0, px[2])
#
#     return image
#
#
# def alg2(image: np.ndarray):
#     for line in image:
#         for px in line:
#             if px[0] < 200 and px[1] < 200 and px[2] < 200:
#                 px[0], px[1], px[2] = 255, 255, 255
#             else:
#                 px[0], px[1], px[2] = 255, 255, 254
#     return image
#
#
# def alg2too(image: np.ndarray):
#     for line in image:
#         for px in line:
#             if px[0] == 255 and px[1] == 255 and px[2] == 254:
#                 px[0], px[1], px[2] = 0, 0, 0
#     return image
#
#
# def alg3(name: str):
#     img = cv.imread(name, 0)
#     img = cv.medianBlur(img, 5)
#     ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
#     th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    # return th1
#
#
# def main():
#     name = r'A:\ProgrammingLanguages\InDeveloping\Python\AlgImg\test.png'
#     img = Image(name)
#     img.image = alg(img.image)
#     img.save_image_cv2(img.image, 'print1')
#
#
# if __name__ == '__main__':
#     main()
