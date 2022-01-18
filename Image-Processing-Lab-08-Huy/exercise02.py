import os
import re
import cv2
import numpy as np
import matplotlib.pyplot as plt

path_source = r'frames/'

# image = cv2.imread(path_source + r'image1.jpg')


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    canny = cv2.Canny(blur, 50, 150)
    return canny


def region_of_interest(image):
    stencil = np.zeros_like(image)
    polygons = np.array([[50, 270], [220, 160], [360, 160], [480, 270]])
    cv2.fillConvexPoly(stencil, polygons, 1)
    masked_image = cv2.bitwise_and(image, image, mask=stencil)
    return masked_image


def display_lines(image, lines):
    line_image = np.zeros_like(image)
    try:
        if len(lines) == 2:
            for x1, y1, x2, y2 in lines:
                # print (x1, y1, x2, y2)
                cv2.line(line_image, (x1, y1), (x2, y2), (255, 255, 0), 2)
    except TypeError:
        print('Error')
    finally:
        return line_image


def make_coordinates(image, line_parameters):
    # if type(line_parameters) == np.float64:
    # cv2.imshow('', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])


def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    # print ('left', left_fit)
    # print ('right', right_fit)
    left_fit_average = np.array(np.average(left_fit, axis=0))
    right_fit_average = np.array(np.average(right_fit, axis=0))
    # if type(left_fit_average) == np.float64:
    #     print (left_fit_average)
    # print ('Left', type(left_fit_average))
    # print ('Right', type(right_fit_average))
    if (len(left_fit) != 0):
        left_line = make_coordinates(image, left_fit_average)
    else:
        left_line = np.array([0, 0, 0, 0])
    if (len(right_fit) != 0):
        right_line = make_coordinates(image, right_fit_average)
    else:
        right_line = np.array([0, 0, 0, 0])
    return np.array([left_line, right_line])

out = cv2.VideoWriter('Output/exercise02.avi', cv2.VideoWriter_fourcc(
    'M', 'J', 'P', 'G'), 30, (480, 270))

# while(cap.isOpened()):
# _, frame = cap.read()
col_frames = os.listdir('frames/')
col_frames.sort(key=lambda f: int(re.sub('\D', '', f)))

# load frames
# col_images=[]
for x in col_frames:
    frame = cv2.imread(path_source+x)
    canny_image = canny(frame)
    cropped_image = region_of_interest(canny_image)
    ret, thresh = cv2.threshold(cropped_image, 130, 145, cv2.THRESH_BINARY)
    lines = cv2.HoughLinesP(thresh, 1, np.pi/180, 30, maxLineGap=200)
    # plt.imshow(thresh)
    # plt.show()
    # cv2.imshow('', cropped_image)
    # print ('Lines:', lines)
    averaged_lines = average_slope_intercept(frame, lines)
    # print (averaged_lines)
    line_image = display_lines(frame, averaged_lines)
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    cv2.putText(combo_image,
                '518H0545_NhutNguyen236',
                (50, 50),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (255, 10, 0),
                1,
                cv2.LINE_AA)
    # print (x)
    out.write(combo_image)
    # cv2.imshow('result',combo_image)
    if cv2.waitKey(1) == ord('q'):
        break

# cap.release()
print('Done')
out.release()
# cv2.destroyAllWindows()

# cv2.imshow('result',combo_image )
# cv2.waitKey(0)
cv2.destroyAllWindows()
