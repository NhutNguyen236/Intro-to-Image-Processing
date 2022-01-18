import cv2 as cv
import matplotlib.pyplot as plt
import numpy
from pathlib import Path


def solver(image):
    rotate = rotator(image)
    shifted = shifter(image)
    edged = edge_detector(image)

    figure = plt.figure()

    Titles = ["Original", "Rotated", "Shifted", "Edge detected"]
    count = 4
    images = [cv.cvtColor(image, cv.COLOR_BGR2RGB), cv.cvtColor(rotate, cv.COLOR_BGR2RGB), cv.cvtColor(
        shifted, cv.COLOR_BGR2RGB), cv.cvtColor(edged, cv.COLOR_BGR2RGB)]

    for i in range(count):
        plt.subplot(2, 2, i + 1)
        plt.title(Titles[i])
        plt.imshow(images[i])

    save_path = (Path(__file__).resolve().parent.parent.parent).joinpath(
        'Result_images')

    figure.savefig(save_path.joinpath('image_11.png'))


def rotator(image):
    M = cv.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), 45, 1)
    res = cv.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return res


def shifter(image):
    ratio = numpy.float32([[1, 0, 300], [0, 1, 100]])

    res = cv.warpAffine(image, ratio, (image.shape[1], image.shape[0]))

    return res


def edge_detector(image):
    return cv.Canny(image, 200, 100)
