import cv2 as cv
import numpy as np

def image_sharpening(image):
    # Sharpen using kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    sharpen_kernel =  cv.filter2D(image, -1, kernel)
    cv.imwrite('Output/sharpen_kernel.jpg', sharpen_kernel)

    # Sharpen using addWeighted
    sharpen_kernel = cv.GaussianBlur(image, (9, 9), 10)
    sharpen_addWeighted = cv.addWeighted(image, 1.5, sharpen_kernel, -0.5, 0)
    cv.imwrite('Output/sharpen_addWeighted.jpg', sharpen_addWeighted)