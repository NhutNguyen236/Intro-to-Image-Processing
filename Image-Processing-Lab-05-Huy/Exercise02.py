import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

def noise_adder(image):
    """
    Add noise to an image
    Input: image
    Output: image with noise
    """

    # Create Gaussian noise with random values
    gauss = np.random.normal(0, 1, image.size)
    gauss = gauss.reshape(image.shape[0], image.shape[1], image.shape[2]).astype('uint8')

    # Add the Gaussian noise to the image
    img_gauss = cv.add(image, gauss)
    cv.imwrite('Output/image_noise.png', img_gauss)

def blur_image(image):
    """
    Blur an image using different methods
    Input: image
    Output: blurred image
    """
    # using built-in function
    blurred_image = cv.blur(image, (5, 5))
    cv.imwrite('Output/blur_builtin.png', blurred_image)

    # Gaussian blurring
    gauss = cv.GaussianBlur(image, (5, 5), 0, 0)
    cv.imwrite('Output/blur_gauss.png', gauss)

    # Median blurring
    median = cv.medianBlur(image, 5)
    cv.imwrite('Output/blur_median.png', median)

    # Bilateral blurring
    bilateral = cv.bilateralFilter(image, 9, 75, 75)
    cv.imwrite('Output/blur_bilteral.png', bilateral)

    # blurring with a kernel
    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv.filter2D(image, -1, kernel)
    cv.imwrite('Output/blur_kernel.png', dst)


    
