import cv2 as cv
from pathlib import Path
import matplotlib.pyplot as plt
import numpy
from .arithmetic import checkSize


def bitwise_calculator(image1_path, image2_path):

    image1 = cv.imread(str(image1_path))
    image2 = cv.imread(str(image2_path))

    image_size1 = image1.shape

    figure = plt.gcf()
    Titles = ["Image 1", "Image2", "AND", "OR", "XOR", "NOT"]
    count = 6

    And = Or = xor = Not = numpy.empty

    if(checkSize(image1, image2) == False):
        # pick image 2 as a default image to resize it to the size of image 1
        # in cv2 resize, height comes before width so I put them there 1 then 0
        new_image2 = cv.resize(image2, (image_size1[1], image_size1[0]))
        And = bit_and(image1, new_image2)
        Or = bit_or(image1, new_image2)
        xor = bit_xor(image1, new_image2)
        Not = bit_not(image1, new_image2)

    else:
        And = bit_and(image1, image2)
        Or = bit_or(image1, image2)
        xor = bit_xor(image1, image2)
        Not = bit_not(image1, image2)

    images = [cv.cvtColor(image1, cv.COLOR_BGR2RGB), cv.cvtColor(image2, cv.COLOR_BGR2RGB), cv.cvtColor(
        And, cv.COLOR_BGR2RGB), cv.cvtColor(Or, cv.COLOR_BGR2RGB), cv.cvtColor(xor, cv.COLOR_BGR2RGB), cv.cvtColor(Not, cv.COLOR_BGR2RGB)]

    for i in range(count):
        plt.subplot(2, 3, i + 1)
        plt.title(Titles[i])
        plt.imshow(images[i])

    plt.show()

    save_path = (Path(__file__).resolve().parent.parent.parent).joinpath(
        'Result_images')

    figure.savefig(str(save_path.joinpath('image_07.png')))


def bit_and(image1, image2):
    return cv.bitwise_and(image2, image1, mask=None)


def bit_or(image1, image2):
    return cv.bitwise_or(image2, image1, mask=None)


def bit_xor(image1, image2):
    return cv.bitwise_xor(image2, image1, mask=None)


def bit_not(image1, image2):
    return cv.bitwise_not(image2, image1, mask=None)
