import matplotlib.pyplot as plt
import cv2 as cv

def show_histogram(image):
    """
    This function will show a histogram of the data in input
    Input: image
    Output: histogram
    """

    histogram = cv.calcHist([image],[0],None,[256],[0,256])

    # show the plotting graph of an image
    plt.plot(histogram)
    plt.show()

def contrast_enhancer(image):
    """
    This function will enhance the contrast of an image
    Input: image
    Output: enhanced image
    """

    # show the histogram of the image
    show_histogram(image)

    # enhance the contrast of the image
    enhanced_img = cv.equalizeHist(image)

    # show the enhanced image
    cv.imshow('Enhanced Image',enhanced_img)

    # show the histogram of the enhanced image
    show_histogram(enhanced_img)

    # wait for any key to be pressed
    cv.waitKey(0)

    # destroy all windows
    cv.destroyAllWindows()
