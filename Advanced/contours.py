import cv2 as cv
import numpy as np
img= cv.imread('Photos/Cat.jpg')
cv.imshow('Cat', img)

#convert to grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)



#blur image
blur= cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#edge detection
canny= cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)


#generate a blank image
blank= np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
'''
finding contours using using the thresholded image
'''
#thresholding
ret, thresh= cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)


contours, hierarchies= cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#contours is a list of all the contours in the image
#hierarchies is the relationship between the contours

print(f'{len(contours)} contours found')


#draw contours on the blank image
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours drawn', blank)


cv.waitKey(0) # 0 means infinite time