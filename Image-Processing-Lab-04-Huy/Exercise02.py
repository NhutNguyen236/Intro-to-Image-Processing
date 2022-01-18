# Using morphological operations and contour to draw rectangles surrounding each number (bounding boxes).
# [x] (1) Convert to binary image (mask of numbers) using thresholding techniques
# [x] (2) Using dilation/closing to connect digits of each numbers (choose a suitable kernel in size)
# [x] (3) Find contours and bounding boxes (using methods in Contour features: boundingRect)

import cv2 as cv
import numpy as np

def exercise02(image):
    # read image
    numbers_img = image

    # convert image to grayscale
    gray_numbers = cv.cvtColor(numbers_img, cv.COLOR_BGR2GRAY)

    # emphasize all numbers
    numbers_mask = cv.threshold(gray_numbers, 0, 255, cv.THRESH_TRIANGLE)[1]
    cv.imshow("All numbers from image", numbers_mask)

    # connect digits to make it a whole number
    kernel = np.ones((7, 7), np.uint8)
    dilation = cv.dilate(numbers_mask, kernel, iterations = 1)
    closing = cv.morphologyEx(dilation, cv.MORPH_CLOSE, kernel)

    # getting contours
    contours, hierarchy = cv.findContours(
        closing, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    numbers_contours = cv.drawContours(
        numbers_img, contours, -1, (0, 255, 0), 1, cv.LINE_AA)

    print(str(len(contours)))

    for c in contours:
        x, y, w, h = cv.boundingRect(c)

        # Make sure contour area is large enough
        if (cv.contourArea(c)) > 10:
            cv.rectangle(numbers_contours, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv.imshow('All contours with bounding box', numbers_contours)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.waitKey()

    # write final image to Output
    cv.imwrite("Output/exercise02.png", numbers_contours)
