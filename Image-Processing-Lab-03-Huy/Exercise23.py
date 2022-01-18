from pathlib import Path
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# read image
IMAGE_PATH = (Path(__file__).resolve().parent).joinpath('numbers.png')


def image_renew():
    """
        This is for when we need to refresh our input image
    """
    return cv.imread(str(IMAGE_PATH), cv.IMREAD_GRAYSCALE)


def ex1():
    """
        Serve exercise 2.3.1
    """

    # greater or equal with 180 are in black and others are white
    # Read image
    src = cv.imread(str(IMAGE_PATH), cv.IMREAD_GRAYSCALE)

    # >= 180
    greater = cv.threshold(src, 150, 255, cv.THRESH_BINARY_INV)[1]
    cv.imwrite("Output/Greater-or-equal-with-180.png", greater)

    # reset image
    src = cv.imread(str(IMAGE_PATH), cv.IMREAD_GRAYSCALE)

    # < 180
    lower_mask = cv.bitwise_not(greater, src, mask=None)

    src = cv.imread(str(IMAGE_PATH), cv.IMREAD_GRAYSCALE)
    th, lower = cv.threshold(src, 150, 255, cv.THRESH_TRIANGLE)

    cv.imshow('es', lower)
    cv.imshow('lower', lower_mask)
    lowers = cv.bitwise_not(lower, lower, mask=lower_mask)
    cv.imwrite("Output/Less-than-180.png", lowers)
    cv.waitKey()


def ex2():
    """
        Serve exercise 2.3.2 with 
    """
    # use thresh triangle to get all the numbers out
    image = cv.imread(str(IMAGE_PATH), cv.IMREAD_GRAYSCALE)

    numbers_mask = cv.threshold(image, 0, 255, cv.THRESH_TRIANGLE)[1]
    cv.imshow('hello1', numbers_mask)

    # using rois to save numbers
    number_rois = cv.selectROIs("Select all the numbers", numbers_mask)

    number_index = 0

    for roi in number_rois:
        x1 = roi[0]
        y1 = roi[1]
        width = roi[2]
        height = roi[3]

        img_crop = numbers_mask[y1:y1+height, x1:x1+width]

        # save cropped image to Output
        cv.imwrite("Output/Numbers/" + str(number_index) + ".png", img_crop)

        number_index += 1


# ex1()
ex2()
