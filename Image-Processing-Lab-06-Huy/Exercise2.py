import cv2 as cv
import numpy as np
from Exercise1 import save_image


def sudoku_detect(img):
    """
        Sudoku grid detect
    """
    # Apply Gaussian Blur
    blur = cv.GaussianBlur(img, (5, 5), 0)
    # Apply Canny Edge Detection
    canny = cv.Canny(blur, 50, 150)
    # Apply Hough Lines
    lines = cv.HoughLines(canny, 1, np.pi/180, 200)
    # Draw lines
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    # Show image
    cv.imshow('Sudoku', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    save_image(img, 'sudoku_detect')


# Read input image in grayscale
input_image = cv.imread('input.png', cv.IMREAD_GRAYSCALE)

sudoku_detect(input_image)
