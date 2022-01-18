import cv2 as cv
from packages.remove_lines import remove_horizontal_lines
from packages.image_crop import crop
from packages.draw_boundingbox import draw_boundingbox

# read image 
img = cv.imread("input.png")
# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray0", gray)

gray = cv.bitwise_not(gray)
cv.imshow("gray1", gray)

w, h = gray.shape
if w % 2 != 0:
    w += 1
elif h % 2 != 0:
    h += 1

wr = w//2
hr = h//2

gray = remove_horizontal_lines(gray)

# divide the image into 4 parts
ls, coordinate = crop(gray, w, h, wr, hr)
roi1, roi2, roi3, roi4 = ls[0], ls[1], ls[2], ls[3]
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))

"""
    Proceess each roi using morphological techniques
"""

# ROI1
roi1 = cv.threshold(roi1, 80, 255, cv.THRESH_BINARY)[1]
cv.imshow("roi1", roi1)
gray[coordinate[0][0]: coordinate[0][2],
     coordinate[0][1]: coordinate[0][3]] = roi1


# ROI2
roi2 = cv.threshold(roi2, 100, 255, cv.THRESH_BINARY)[1]

roi2 = cv.morphologyEx(roi2, cv.MORPH_OPEN, kernel, iterations=1)
gray[coordinate[1][0]: coordinate[1][2],
     coordinate[1][1]: coordinate[1][3]] = roi2

# ROI3
roi3 = cv.threshold(roi3, 100, 255, cv.THRESH_BINARY)[1]
gray[coordinate[2][0]: coordinate[2][2],
     coordinate[2][1]: coordinate[2][3]] = roi3

# xu ly roi4
roi4 = cv.threshold(roi4, 252, 255, cv.THRESH_BINARY)[1]
roi4 = cv.morphologyEx(roi4, cv.MORPH_CLOSE, kernel, iterations=2)

# ROI4 has a lot of noises so we need to break it down to smaller pieces
w_r4, h_r4 = roi4.shape
ls_r4, coordinate_r4 = crop(roi4, w_r4, h_r4, w_r4//2, h_r4//2)

# roi4_p1
ls_r4[0] = cv.morphologyEx(
    ls_r4[0], cv.MORPH_CLOSE, kernel, iterations=1)
ls_r4[0] = cv.dilate(ls_r4[0], kernel, iterations=3)
ls_r4[0] = cv.erode(ls_r4[0], kernel, iterations=1)
roi4[coordinate_r4[0][0]: coordinate_r4[0][2],
     coordinate_r4[0][1]: coordinate_r4[0][3]] = ls_r4[0]

# roi4_p2
ls_r4[1] = cv.morphologyEx(
    ls_r4[1], cv.MORPH_CLOSE, kernel, iterations=2)
ls_r4[1] = cv.dilate(ls_r4[1], kernel, iterations=3)
ls_r4[1] = cv.erode(ls_r4[1], kernel, iterations=1)

roi4[coordinate_r4[1][0]: coordinate_r4[1][2],
     coordinate_r4[1][1]: coordinate_r4[1][3]] = ls_r4[1]

# roi4_p3
ls_r4[2] = cv.morphologyEx(
    ls_r4[2], cv.MORPH_CLOSE, kernel, iterations=1)
ls_r4[2] = cv.dilate(ls_r4[2], kernel, iterations=1)
roi4[coordinate_r4[2][0]: coordinate_r4[2][2],
     coordinate_r4[2][1]: coordinate_r4[2][3]] = ls_r4[2]

# roi_p4
ls_r4[3] = cv.morphologyEx(
    ls_r4[3], cv.MORPH_CLOSE, kernel, iterations=2)
ls_r4[3] = cv.dilate(ls_r4[3], kernel, iterations=1)
roi4[coordinate_r4[3][0]: coordinate_r4[3][2],
     coordinate_r4[3][1]: coordinate_r4[3][3]] = ls_r4[3]

gray[coordinate[3][0]: coordinate[3][2],
     coordinate[3][1]: coordinate[3][3]] = roi4

output, bounding_boxes = draw_boundingbox(gray, img)

# write down the coordinates of the bounding boxes
f = open('Output/output.txt', 'w')
for i in bounding_boxes:
    f.write(str(i)+"\n")
f.close()

cv.imshow("output", output)
cv.imwrite("Output/output.png", output)
cv.waitKey(0)
