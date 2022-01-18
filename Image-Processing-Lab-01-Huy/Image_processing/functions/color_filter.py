from pathlib import Path
import cv2 as cv
import matplotlib.pyplot as plt
import numpy


def color_filter(image):
    """
        Filter colors from a color
        Input: BGR images
        Output: plot results using matplotlib 
    """

    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # define lower and upper bounds for colors
    # remember that those arrays follow BGR rule

    white_lower = numpy.array([0, 0, 128])
    white_upper = numpy.array([97, 105, 255])

    # create color masks
    white_mask = cv.inRange(hsv, white_lower, white_upper)

    white = cv.bitwise_and(image, image, mask = white_mask)

    figure = plt.figure()

    Titles = ["Original", "White filter"]
    count = 2
    images = [cv.cvtColor(image, cv.COLOR_BGR2RGB), cv.cvtColor(white, cv.COLOR_BGR2RGB)]

    for i in range(count):
        plt.subplot(1, 2, i + 1)
        plt.title(Titles[i])
        plt.imshow(images[i])

    save_path = (Path(__file__).resolve().parent.parent.parent).joinpath(
        'Result_images')

    figure.savefig(save_path.joinpath('image_13.png'))
