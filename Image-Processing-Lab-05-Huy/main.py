# Import functions for the main program
from Exercise01 import *
from Exercise02 import *
from Exercise03 import *
from Exercise04 import *

# Import libs
import cv2 as cv

# Read image with grayscale
input_image = cv.imread('waterfall.png', cv.IMREAD_GRAYSCALE)

# Read image with color
image = cv.imread('waterfall.png')

###################### Exercise01 #############################
# Show image histogram in gray scale
show_histogram(input_image)

# Enhance contrast of the image
contrast_enhancer(input_image)

###################### Exercise02 #############################
# Add noise to the image
noise_adder(image)

# Blur the image
blur_image(image)

###################### Exercise03 #############################
# Sharpening the image
image_sharpening(image)

###################### Exercise04 #############################
# motion motion_estimation
motion_estimation()