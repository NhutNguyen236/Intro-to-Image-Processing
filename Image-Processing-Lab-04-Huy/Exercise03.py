"""
Using morphological operations and contour to draw rectangles surrounding each digit (bounding boxes).

(1) Convert to binary image (mask of numbers) using thresholding techniques 
(2) Using opening and closing to remove noise and connect broken digits
(3) Using dilation to connect digits of each numbers (choose a suitable kernel in size)

"""

import cv2 as cv
import numpy as np

def exercise03(image):
    # read image
    numbers_img = image

    # convert image to grayscale
    gray_numbers = cv.cvtColor(numbers_img, cv.COLOR_BGR2GRAY)

    # convert to binary 
    thresh = cv.threshold(gray_numbers, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]

    # create kernel
    kernel = np.ones((1, 1), np.uint8)

    # connect digits to make it a whole number
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)

    # getting contours
    contours, hierarchy = cv.findContours(
        opening, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    numbers_contours = cv.drawContours(
        numbers_img, contours, -1, (0, 255, 0), 1, cv.LINE_AA)

    for c in contours:
        x, y, w, h = cv.boundingRect(c)

        # Make sure contour area is large enough
        if (cv.contourArea(c)) > 20:
            cv.rectangle(numbers_contours, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv.imshow('All contours with bounding box', numbers_contours)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.waitKey()

    # write final image to Output
    cv.imwrite("Output/exercise03.png", numbers_contours)