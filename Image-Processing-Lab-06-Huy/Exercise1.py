import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

def save_image(img, name):
    """
        Save image
    """
    cv.imwrite('Output/' + name + '.png', img)

def canny_edge_detection(img):
    """
        Canny edge detection
    """
    edges = cv.Canny(img, 50, 150, apertureSize=3)
    cv.imshow('Edges', edges)
    cv.waitKey(0)

    save_image(edges, 'canny_edge_detection')

def sobel_edge_detection(img):
    """
        Sobel edge detection
    """
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
    abs_sobelx = cv.convertScaleAbs(sobelx)
    abs_sobely = cv.convertScaleAbs(sobely)
    sobel_edge = cv.addWeighted(abs_sobelx, 0.5, abs_sobely, 0.5, 0)
    cv.imshow('Sobel', sobel_edge)
    cv.waitKey(0)

    save_image(sobel_edge, 'sobel_edge_detection')

def hough_line_detection(img):
    """
        Line detection using Hough transform
    """
    edges = cv.Canny(img, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=100, maxLineGap=10)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    cv.imshow('Hough', img)
    cv.waitKey(0)

    save_image(img, 'hough_line_detection')

def circle_detection(img):
    """
        Coin detection using Hough transform
    """
    # blur image
    img = cv.medianBlur(img, 5)
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 40, param1=50, param2=30, minRadius=1, maxRadius=60)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv.circle(img, (i[0], i[1]), i[2], (0, 255, 100), 2)
    cv.imshow('Circles', img)
    cv.waitKey(0)

    save_image(img, 'circle_detection')