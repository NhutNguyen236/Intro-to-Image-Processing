import cv2
import numpy as np
 
# load image and start video
foreground = cv2.imread('TDT_logo.png')
cap = cv2.VideoCapture("my_cam.mp4")

# init font
font = cv2.FONT_HERSHEY_SIMPLEX

# position of logo on video
top_left = [0, 0] # the top-left corner of your logo goes here
tx = top_left[0] # less typing later
ty = top_left[1]

# crop of logo
left = 0
right = 100
top = 0 # y = 0 is the top of the image
bottom = 100

# calculate width and height of logo crop
width = right - left
height = bottom - top

# main loop
alpha = 0.1
while True:
    # read image
    ret, background = cap.read()

    # horizontal flip to create mirror image
    background = cv2.flip(background,1)

    # quick primer on 2d image slicing:
    # images are [y,x]
    # crop = image[0:100, 300:500] will be a 200x100 image (width x height) 
    # the logo slice should give you a decent idea of what's going on

    # WARNING: there are no out-of-bounds checks here, make sure that
    # tx + width is less than the width of the background
    # ty + height is less than the height of the background
    # right is less than the width of the foreground
    # bottom is less than the height of the foreground

    # get crops of background and logo
    background_slice = background[ty:ty+height, tx:tx+width]; 
    logo_slice = foreground[top:bottom, left:right]; 

    # since we don't change our crop, we could do the logo slice outside the loop
    # but I'll keep it here for clarity

    # add slice of logo onto slice of background
    added_image = cv2.addWeighted(background_slice,alpha,logo_slice,1-alpha,0)
    background[ty:ty+height, tx:tx+width] = added_image

    # show image
    cv2.imshow('My webcam record but itz not me but itz my webcam :D', background)
    k = cv2.waitKey(10)

    # process keypresses
    if k == ord('q'):
        break
    if k == ord('a'):
        alpha +=0.1
        if alpha >=1.0:
            alpha = 1.0
    elif k== ord('d'):
        alpha -= 0.1
        if alpha <=0.0:
            alpha = 0.0

# close
cap.release()
cv2.destroyAllWindows()