import cv2
import numpy as np
from imutils import contours

# read image 
image = cv2.imread('numbers.png')

# create mask 
mask = np.zeros(image.shape[::2], dtype=np.uint8)

# convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_TRIANGLE | cv2.THRESH_BINARY_INV)[1]
cv2.imshow('thresh', thresh)

cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
(cnts, _) = contours.sort_contours(cnts, method="left-to-right")

ROI_number = 0
for c in cnts:
    area = cv2.contourArea(c)
    if area < 800 and area > 200:
        x,y,w,h = cv2.boundingRect(c)
        ROI = 255 - thresh[y:y+h, x:x+w]
        cv2.drawContours(mask, [c], -1, (255,255,255), -1)
        cv2.imwrite('ROI_{}.png'.format(ROI_number), ROI)
        ROI_number += 1

cv2.imshow('mask', mask)
cv2.imshow('thresh', thresh)
cv2.waitKey()