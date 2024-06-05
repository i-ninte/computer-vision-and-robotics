'''

in this script we will draw shapes and input text on images and videos with opencv
'''

import cv2 as cv
import numpy as np

# Create a blank image
blank_image= np.zeros((500,500,3),dtype='uint8' )
#because we are giving the image a width, heght and the number of channels ie rgb
#uint8 is the data type of the image
cv.imshow('Blank',blank_image)

# 1. Paint the image a certain color
blank_image[:]= 0,255,0
cv.imshow('Green',blank_image)
#paint certain part of the image a certain color
blank_image[200:300,300:400]= 0,0,255
cv.imshow('Red',blank_image)


#write text on the image
cv.putText(blank_image,'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text',blank_image)

cv.waitKey(0) # 0 means infinite time