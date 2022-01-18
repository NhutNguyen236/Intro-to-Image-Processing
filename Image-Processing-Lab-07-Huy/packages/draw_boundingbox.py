import cv2 as cv

def draw_boundingbox(gray, img):
    contours, _ = cv.findContours(
        gray.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    boundingBoxes = []
    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)
        area_contours = cv.contourArea(cnt)
        
        # contour filter upto 40
        if area_contours > 40:
            boundingBoxes.append((x, y, w, h))
            output = cv.rectangle(img, (x, y), (x+w, h+y), (0, 0, 255), 2)
    return output, boundingBoxes