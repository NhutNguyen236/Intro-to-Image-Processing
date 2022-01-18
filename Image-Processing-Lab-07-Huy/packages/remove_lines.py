import cv2 as cv

def remove_horizontal_lines(gray):
    """
        Remove horizontal lines from the gray image
    """
    thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
    cv.imshow('thresh', thresh)
    
    # get horizontal lines mask
    horizontal_mask = cv.getStructuringElement(cv.MORPH_RECT, (25, 1))
    cv.imshow('horizontal_mask', horizontal_mask)
    
    lines = cv.morphologyEx(thresh, cv.MORPH_OPEN,
                             horizontal_mask, iterations=2)
    cv.imshow('lines', lines)

    cnts_lines, _ = cv.findContours(
        lines, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    print(cnts_lines)

    for c in cnts_lines:
        cv.drawContours(gray, [c], -1, (0, 0, 0), 3)

    cv.imshow('remove_horizontal_lines', gray)
    return gray