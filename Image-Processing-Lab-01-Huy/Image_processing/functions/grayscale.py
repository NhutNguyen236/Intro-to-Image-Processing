from pathlib import Path
import cv2 as cv
import matplotlib.pyplot as plt
import numpy

def create_grayscale(image):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    image_label = cv.putText(
        gray_image, "Grayscaling of Images", (100, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)

    cv.imshow("Grayscaling of Images", image_label)

    cv.waitKey()

    save_path = (Path(__file__).resolve().parent.parent.parent).joinpath(
        'Result_images')

    cv.imwrite(str(save_path.joinpath('image_10.png')), image_label)

    
