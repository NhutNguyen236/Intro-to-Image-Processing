##################### Modules import ##############################
from Image_processing.functions.resize import resizer
from Image_processing.functions.make_border import border_maker
from Image_processing.functions.grayscale import create_grayscale
from Image_processing.functions.scaling_rotating_shifting_edgeDet import solver
from Image_processing.functions.colors_convert import color_converter
from Image_processing.functions.color_filter import color_filter
from Image_processing.functions.visualizer import colors_visualizer
import cv2 as cv
from pathlib import Path
from Getting_Started.functions.read_display_write_image import read_image, write_image, show_image
from Getting_Started.functions.color_space import rgb_splitter
from Getting_Started.functions.arithmetic import arithmetic
from Getting_Started.functions.bitwise import bitwise_calculator
from Drawing import drawer
import matplotlib.pyplot as plt

##################### Image import ##############################
IMAGE_PATH = (Path(__file__).resolve().parent).joinpath('Peter.png')
SAVE_PATH = (Path(__file__).resolve().parent).joinpath('Result_images')
SPIDER_LOGO = (Path(__file__).resolve().parent).joinpath('spider_logo.png')

# Exercise 01, 02, 03
read_image(IMAGE_PATH)
show_image(cv.imread(str(IMAGE_PATH)),
           'Display an image in OpenCV using Python')
write_image(IMAGE_PATH, 'image_03.png')

# Exercise 05
rgb_splitter(cv.imread(str(IMAGE_PATH)), SAVE_PATH.joinpath('image_05.png'))

# Exercise 06
arithmetic(IMAGE_PATH, SPIDER_LOGO)

# Exercise 07
bitwise_calculator(IMAGE_PATH, SPIDER_LOGO)

# Exercise 08
resizer(cv.imread(str(IMAGE_PATH)))

# Exercise 09
border_maker(cv.imread(str(IMAGE_PATH)))

# Exercise 10
create_grayscale(cv.imread(str(IMAGE_PATH)))

# Exercise 11
solver(cv.imread(str(IMAGE_PATH)))

# Exercise 12
color_converter(cv.imread(str(IMAGE_PATH)))

# Exercise 13
color_filter(cv.imread(str(SPIDER_LOGO)))

# Exercise 14
colors_visualizer(cv.imread(str(IMAGE_PATH)))

# Exercise 15
drawer.draw_line(cv.imread(str(IMAGE_PATH)))

# Exercise 16
drawer.draw_arrow(cv.imread(str(IMAGE_PATH)))

# Exercise 17
drawer.draw_circle(cv.imread(str(IMAGE_PATH)))

# Exercise 18
drawer.draw_rectangle(cv.imread(str(IMAGE_PATH)))

# Exercise 19
drawer.draw_ellipse(cv.imread(str(IMAGE_PATH)))

# Exercise 20
drawer.texting_img(cv.imread(str(IMAGE_PATH)))




