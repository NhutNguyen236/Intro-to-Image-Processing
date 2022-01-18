from pathlib import Path
import numpy as np
import cv2 as cv


# Read image
IMAGE_PATH = (Path(__file__).resolve().parent).joinpath('Sample.png')
image = cv.imread(str(IMAGE_PATH))

mask = np.zeros(image.shape[:2], dtype="uint8")
print(mask)

# before masking a circle in, we need to select face rois
# rois_face = cv.selectROIs("Select faces from Sample", image)

# print(rois_face)
# for roi in rois_face:
#     x1 = roi[0]
#     y1 = roi[1]
#     width = roi[2]
#     height = roi[3]

# where the pixeLs are vaLued at 255
cv.circle(mask, (239, 418), 132, 255, -1)
cv.circle(mask, (731, 326), 132, 255, -1)
cv.circle(mask, (1207, 479), 132, 255, -1)
cv.imshow('',mask)

# performing a bitwise_and with the image and the mask
masked = cv.bitwise_and(image, image, mask=mask)

save_path = (Path(__file__).resolve().parent).joinpath(
    'Output')
cv.imwrite(str(save_path.joinpath('image_21.png')), masked)
cv.imshow( "Mask appLied to Tmage", masked)
cv.waitKey()
