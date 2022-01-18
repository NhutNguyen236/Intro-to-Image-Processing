from Exercise01 import sudoku_adaptive, sudoku_otsu
from Exercise02 import exercise02
from Exercise03 import exercise03

import cv2 as cv

# read image in grayscale mode sudoku image
sudoku_img = cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE)

# read exercise 02 image
numbers_img = cv.imread('numbers.png')

# read exercise 03 image
xskt = cv.imread('xskt.png')

# Exercise 01
sudoku_adaptive(sudoku_img)
sudoku_otsu(sudoku_img)

# Exercise 02
exercise02(numbers_img)

# Exercise03
exercise03(xskt)