import cv2 as cv
from pathlib import Path

save_path = (Path(__file__).resolve().parent.parent).joinpath('Result_images')

IMAGE_PATH = (Path(__file__).resolve().parent.parent).joinpath('Peter.png')


def draw_line(image):
    lined_image = cv.line(
        image, (0, 0), (image.shape[0], image.shape[0]), (0, 0, 255), 6)

    marked = cv.putText(lined_image, 'Draw a line', (50, 50), cv.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv.LINE_AA)
    cv.imshow('Line', marked)
    cv.waitKey()
    cv.imwrite(str(save_path.joinpath('image_15.png')), marked)


def draw_arrow(image):
    arrowed_image = cv.arrowedLine(
        image, (0, 0), (image.shape[0], image.shape[0] - 100), (0, 0, 255), 6)

    marked = cv.putText(arrowed_image, 'Draw arrow segment', (50, 50), cv.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv.LINE_AA)
    cv.imshow('Arrow', marked)
    cv.waitKey()
    cv.imwrite(str(save_path.joinpath('image_16.png')), marked)


def draw_circle(image):
    """
        Draw circle to the input image
    """
    # center coordinates with coordinates of (0,0) is always at the top right
    # corner of the image
    center_coordinates = (100, 100)

    radius = 20

    # This rules by BGR so this will be red
    color = (0, 0, 255)

    thickness = 100

    circled_img = cv.circle(image, center_coordinates,
                            radius, color, thickness)

    marked = cv.putText(circled_img, 'Draw a circle', (200, 200), cv.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv.LINE_AA)

    # imshow() only works with waitKey()
    cv.imshow('Circle', marked)
    cv.waitKey()
    cv.imwrite(str(save_path.joinpath('image_18.png')), marked)


def draw_rectangle(image):
    """
        Draw rectangle to the input image
    """
    # center coordinates with coordinates of (0,0) is always at the top right
    # corner of the image
    start_point = (5, 7)

    end_point = (220, 250)

    # This rules by BGR so this will be red
    color = (0, 0, 255)

    thickness = 2

    rectangle_image = cv.rectangle(
        image, start_point, end_point, color, thickness)

    marked = cv.putText(rectangle_image, 'Draw a rectangle', (50, 50), cv.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv.LINE_AA)
    # imshow() only works with waitKey()
    cv.imshow('Rectangle', marked)
    cv.waitKey()
    cv.imwrite(
        str(save_path.joinpath('image_19.png')), marked)


def draw_ellipse(image):
    """
        Draw eclipse to the input image
    """
    # center coordinates with coordinates of (0,0) is always at the top right
    # corner of the image
    center_coordinates = (200, 200)

    axesLength = (100, 50)

    angle = 0

    startAngle = 0

    endAngle = 360

    # This rules by BGR so this will be red
    color = (0, 0, 255)

    thickness = 2

    ellipsed_image = cv.ellipse(
        image, center_coordinates, axesLength, angle, startAngle, endAngle, color, thickness)

    marked = cv.putText(ellipsed_image, 'Draw a ellipse', (50, 50), cv.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv.LINE_AA)

    # imshow() only works with waitKey()
    cv.imshow('Ellipse', marked)
    cv.waitKey()
    cv.imwrite(
        str(save_path.joinpath('image_17.png')), marked)


def texting_img(image):
    # font
    font = cv.FONT_HERSHEY_SIMPLEX

    # org
    org = (50, 50)

    # fontScale
    fontScale = 1

    # RED color in BGR
    color = (0, 0, 255)

    # Line thickness of 2 px
    thickness = 2

    # State out message
    message = 'Draw a text string'

    # Using cv2.putText() method
    texted_image = cv.putText(image, message, org, font,
                              fontScale, color, thickness, cv.LINE_AA)

    cv.imshow('Texting', texted_image)
    cv.waitKey()
    cv.imwrite(str(save_path.joinpath('image_20.png')), texted_image)
