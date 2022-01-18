# Blend the following 2 images to create a new image
from pathlib import Path
import numpy as np
import cv2 as cv

# read logo and sample
IMAGE_PATH = (Path(__file__).resolve().parent).joinpath('Sample.png')
LOGO_PATH = (Path(__file__).resolve().parent).joinpath('TDT_logo.png')

image1 = cv.imread(str(IMAGE_PATH))
image2 = cv.imread(str(LOGO_PATH))

# resize image 02 but you can resize 01 too
image2 = cv.resize(image2, image1.shape[1::-1])

overlay = cv.addWeighted(image1, 0.5, image2, 0.5, 0)
save_path = (Path(__file__).resolve().parent).joinpath(
    'Output')
print(save_path)
cv.imwrite(str(save_path.joinpath('image_22.png')), overlay)
cv.imshow('Overlayed', overlay)
cv.waitKey()
cv.destroyAllWindows()
