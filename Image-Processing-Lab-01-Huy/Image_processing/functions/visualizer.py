from pathlib import Path
import cv2 as cv
import matplotlib.pyplot as plt
import numpy


def colors_visualizer(image):
    """
        Convert BGR image to different color spaces
        Input: BGR images
        Output: plot results using matplotlib 
    """
    figure = plt.figure()

    gray = grayScaler(image)
    hsv = hsvConverter(image)
    hls = hlsConverter(image)
    ycrb = ycrbConverter(image)
    sff = sffConverter(image)

    Titles = ["Original", "Grayscale", "HSV", "HLS", "ycrb", "64F"]
    count = 6
    images = [cv.cvtColor(image, cv.COLOR_BGR2RGB), gray, hsv, hls, ycrb, sff]

    for i in range(count):
        plt.subplot(2, 3, i + 1)
        plt.title(Titles[i])
        plt.imshow(images[i])

    save_path = (Path(__file__).resolve().parent.parent.parent).joinpath(
        'Result_images')

    figure.savefig(save_path.joinpath('image_14.png'))


def grayScaler(image):
    gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    return cv.cvtColor(gray_img, cv.COLOR_BGR2RGB)


def hsvConverter(image):
    hsv_img = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    return cv.cvtColor(hsv_img, cv.COLOR_BGR2RGB)


def hlsConverter(image):
    lab_img = cv.cvtColor(image, cv.COLOR_BGR2HLS)

    return cv.cvtColor(lab_img, cv.COLOR_BGR2RGB)

def ycrbConverter(image):
    gray_img = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)

    return cv.cvtColor(gray_img, cv.COLOR_BGR2RGB)


def sffConverter(image):
    hsv_img = cv.Laplacian(image, cv.CV_64F)

    return hsv_img
