# Import functions for the main program
from Exercise1 import *
from Exercise2 import *
# from Exercise03 import *
# from Exercise04 import *

# Import libs
import cv2 as cv

# Read input image in grayscale
input_image = cv.imread('input.png', cv.IMREAD_GRAYSCALE)

# Read coin input for circle detection
coin_input = cv.imread('coin_input.png', cv.IMREAD_GRAYSCALE)

# Exercise 01
canny_edge_detection(input_image)
sobel_edge_detection(input_image)
hough_line_detection(input_image)
circle_detection(coin_input)

# Exercise02
sudoku_detect(input_image)