import cv2 as cv
from pathlib import Path


def border_maker(image):

    # Using cv2.copyMakeBorder() method
    bordered_image = cv.copyMakeBorder(
        image, 10, 10, 10, 10, cv.BORDER_CONSTANT, None, value=[255, 0, 0])

    # Write req to image
    texted_image = cv.putText(bordered_image, 'Create Border around Images',
                            (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv.LINE_AA)

    # Displaying the image
    cv.imshow('Create Border around Images', bordered_image)
    cv.waitKey()

    # save result images
    save_path = (Path(__file__).resolve().parent.parent.parent).joinpath(
        'Result_images')

    # always convert your windowspath to str
    writer = cv.imwrite(str(save_path.joinpath('image_09.png')), bordered_image)

    return writer
