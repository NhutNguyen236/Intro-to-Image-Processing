# Using thresholding techniques to convert
# the grayscale image into a binary image.
import cv2 as cv

def sudoku_adaptive(sudoku_img):
    """
        Do convert sudoku grayscale image
        to binary image
    """
    thresh_mean = cv.adaptiveThreshold(sudoku_img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 5)
    # thresh_gauss = cv.adaptiveThreshold(sudoku_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 150, 5)

    cv.imwrite('Output/binary_sudoku_mean.png', thresh_mean)
    # cv.imwrite('Output/adaptive_binary_sudoku.png', thresh_gauss)

def sudoku_otsu(sudoku_img):
    """
        Do convert sudoku grayscale image
        to binary image using otsu thresh
    """
    # otsu apply
    otsu_thresh = cv.threshold(sudoku_img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

    cv.imwrite('Output/otsu_binary_sudoku.png', otsu_thresh)
