############################################################
#### Read, show, save an image and files with cv2 ##########
############################################################
import cv2 as cv
from pathlib import Path


def read_image(image_path):
    """
        Read image from defined path with input image
        Input: Image name
        Output: image reading map
    """
    # get image exact path and convert to string for imread
    img_src = str(image_path)
    image = cv.imread(img_src)

    image_label = cv.putText(
        image, "Reading an image in OpenCV using Python", (100, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
    cv.imshow("Reading an image in OpenCV using Python", image_label)

    save_path = (Path(__file__).resolve().parent.parent.parent).joinpath(
        'Result_images')

    # always convert your windowspath to str
    cv.imwrite(str(save_path.joinpath('image_01.png')), image_label)

    return image


def show_image(image, img_title):
    # put text to image before showing it
    image = cv.putText(
        image, "Display an image in OpenCV using Python", (100, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
    save_path = (Path(__file__).resolve().parent.parent.parent).joinpath(
        'Result_images')

    # always convert your windowspath to str
    cv.imwrite(str(save_path.joinpath('image_02.png')), image)
    # display image using imshow from opencv
    cv.imshow(img_title, image)
    cv.waitKey(0)


def write_image(image_path, image_name):
    """
        Write image to a defined path
        Input: Image path
    """
    image = cv.imread(str(image_path))

    save_path = (Path(__file__).resolve().parent.parent.parent).joinpath(
        'Result_images')

    # write text to image03
    write_image = cv.putText(
        image, "Writing an image in OpenCV using Python", (100, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

    # always convert your windowspath to str
    writer = cv.imwrite(str(save_path.joinpath(image_name)), write_image)
    writer = cv.imwrite(str(save_path.joinpath('image_04.png')), write_image)

    if(writer == True):
        print(image_name + " saved successfully")
    else:
        print(image_name + " saved FAILED")

    return writer
