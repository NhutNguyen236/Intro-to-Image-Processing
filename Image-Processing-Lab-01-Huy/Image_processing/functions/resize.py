from pathlib import Path
import cv2 as cv
import matplotlib.pyplot as plt


def resizer(image):
    half = cv.resize(image, (0, 0), fx=0.1, fy=0.1)
    bigger = cv.resize(image, (1050, 1610))

    stretch_near = cv.resize(image, (780, 540),
                             interpolation=cv.INTER_NEAREST)

    figure = plt.figure()
    Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
    images = [cv.cvtColor(image, cv.COLOR_BGR2RGB), cv.cvtColor(half, cv.COLOR_BGR2RGB), cv.cvtColor(
        bigger, cv.COLOR_BGR2RGB), cv.cvtColor(stretch_near, cv.COLOR_BGR2RGB)]
    count = 4

    for i in range(count):
        plt.subplot(2, 2, i + 1)
        plt.title(Titles[i])
        plt.imshow(images[i])

    plt.show()

    save_path = (Path(__file__).resolve().parent.parent.parent).joinpath(
        'Result_images')

    figure.savefig(str(save_path.joinpath('image_08.png')))
