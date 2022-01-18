import cv2 as cv
from pathlib import Path
import matplotlib.pyplot as plt
import numpy


def checkSize(image1, image2):

    # get images shapes
    image1_size = image1.shape
    image2_size = image2.shape

    if(image1_size[0] != image2_size[0] or image2_size[1] != image1_size[1]):
        return False
    else:
        return True


def arithmetic(image1_path, image2_path):

    image1 = cv.imread(str(image1_path))
    image2 = cv.imread(str(image2_path))

    image1_size = image1.shape

    figure1 = plt.gcf()
    Titles = ["Image 1", "Image2", "Addition", "Subtraction"]
    count = 4

    # create empty addition and subtraction array
    add = sub = numpy.empty

    if(checkSize(image1, image2) == False):
        # pick image 2 as a default image to resize it to the size of image 1
        # in cv2 resize, height comes before width so I put them there 1 then 0
        new_image2 = cv.resize(image2, (image1_size[1], image1_size[0]))
        add = addition(image1, new_image2)
        sub = subtraction(image1, new_image2)
    else:
        add = addition(image1, image2)
        sub = subtraction(image1, image2)

    images = [cv.cvtColor(image1, cv.COLOR_BGR2RGB), cv.cvtColor(
        image2, cv.COLOR_BGR2RGB), cv.cvtColor(add, cv.COLOR_BGR2RGB), cv.cvtColor(sub, cv.COLOR_BGR2RGB)]

    for i in range(count):
        plt.subplot(2, 2, i + 1)
        plt.title(Titles[i])
        plt.imshow(images[i])

    plt.show()

    save_path = (Path(__file__).resolve().parent.parent.parent).joinpath(
        'Result_images')

    figure1.savefig(str(save_path.joinpath('image_06.png')))

    cv.destroyAllWindows()


def addition(image1, image2):
    sumImage = cv.addWeighted(image1, 0.5, image2, 0.4, 0)

    return sumImage


def subtraction(image1, image2):
    subtractImage = cv.subtract(image1, image2)
    return subtractImage
