from pathlib import Path
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

# Read image
IMAGE_PATH = (Path(__file__).resolve().parent).joinpath('baloon.png')
BALOON_V2 = (Path(__file__).resolve().parent).joinpath('baloon_2.png')


def channels_splitter(image):
    """
        Split channels from image
    """
    B, G, R = cv.split(image)

    Titles = ["Original", "Red", "Green", "Blue"]
    images = [cv.cvtColor(image, cv.COLOR_BGR2RGB), cv.cvtColor(
        R, cv.COLOR_BGR2RGB), cv.cvtColor(G, cv.COLOR_BGR2RGB), cv.cvtColor(B, cv.COLOR_BGR2RGB)]
    count = 4

    for i in range(count):
        plt.subplot(2, 2, i + 1)
        plt.title(Titles[i])
        plt.imshow(images[i])

    plt.show()

    cv.destroyAllWindows()


def baloons_detector(image):
    """
       Detect and bound boxes on baloons
    """

    # clone image
    detected_image = image

    # Select many bloon positions
    rois_image = cv.selectROIs("Select baloon Rois", detected_image)

    # counter to save image with different name
    baloon_numb = 0

    # loop over every bounding box save in array "ROIs"
    baloon_dict = {0: "Yellow", 1: "Blue", 2: "Red", 3: "Green", 4: "Orange"}

    for rect in rois_image:
        x1 = rect[0]
        y1 = rect[1]
        width = rect[2]
        height = rect[3]

        print(rect)

        # draw rectangle according to ratios
        cv.rectangle(detected_image, (x1, y1), (x1 + width,
                     y1 + height), (0, 0, 255), 2)
        # put a text on them too
        cv.putText(detected_image, baloon_dict[baloon_numb], (x1, y1),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

        baloon_numb = baloon_numb + 1

    cv.imshow("Baloons detected", detected_image)
    # hold window
    cv.waitKey(0)


def yellow_extract(image):
    yellow_roi = cv.selectROI("Select Yellow baloon", image)

    yellow_cropped = image[int(yellow_roi[1]):int(
        yellow_roi[1]+yellow_roi[3]), int(yellow_roi[0]):int(yellow_roi[0]+yellow_roi[2])]

    cv.imshow("Yellow baloon extracted", yellow_cropped)

    cv.waitKey()


def yellow_hsv_extractor(image):
    # first convert image to hsv space
    lab_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    low_yellow = np.array([20, 100, 100])
    high_yellow = np.array([30, 255, 255])

    mask = cv.inRange(lab_image, low_yellow, high_yellow)
    inv_mask = cv.bitwise_not(mask)

    res = cv.bitwise_and(image, image, mask=mask)    
    background = cv.bitwise_and(image, image, mask = inv_mask)
    
    cv.imshow("LAB", res)

    green_turner = res.copy()
    green_turner[mask > 0] = (50,205,50)

    added_img = cv.add(green_turner, background)

    cv.imshow("turner", green_turner)

    cv.imshow("final", added_img)

    cv.waitKey()

    return res

def rotate_first_balooon(image):
    # get roi of the baloon you want to rotate
    baloon_roi = cv.selectROI("Select a baloon to rotate", image)

    print(baloon_roi)



###################### EXECUTION ###########################
# channels_splitter(cv.imread(str(IMAGE_PATH)))
# baloons_detector(cv.imread(str(IMAGE_PATH)))
# yellow_extract(cv.imread(str(IMAGE_PATH)))
# yellow_hsv_extractor(cv.imread(str(IMAGE_PATH)))
rotate_first_balooon(cv.imread(str(IMAGE_PATH)))
