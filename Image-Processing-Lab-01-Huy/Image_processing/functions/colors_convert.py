from pathlib import Path
import cv2 as cv
import matplotlib.pyplot as plt
import numpy

def color_converter(image):
    """
        Convert BGR image to different color spaces
        Input: BGR images
        Output: plot results using matplotlib 
    """
    figure = plt.figure()

    gray = grayScaler(image)
    hsv = hsvConverter(image)
    hls = hlsConverter(image)

    Titles = ["Original", "Grayscale", "HSV", "HLS"]
    count = 4
    images = [cv.cvtColor(image, cv.COLOR_BGR2RGB), gray, hsv, hls]

    for i in range(count):
        plt.subplot(2, 2, i + 1)
        plt.title(Titles[i])
        plt.imshow(images[i])

    save_path = (Path(__file__).resolve().parent.parent.parent).joinpath(
        'Result_images')

    figure.savefig(save_path.joinpath('image_12.png'))

def grayScaler(image):
    gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    cv.imshow("gray", gray_img)
    cv.imshow("ori", image)
    cv.waitKey()

    return cv.cvtColor(gray_img, cv.COLOR_BGR2RGB)


def hsvConverter(image):
    hsv_img = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    return cv.cvtColor(hsv_img, cv.COLOR_BGR2RGB)

def hlsConverter(image):
    lab_img = cv.cvtColor(image, cv.COLOR_BGR2HLS)

    return cv.cvtColor(lab_img, cv.COLOR_BGR2RGB)

