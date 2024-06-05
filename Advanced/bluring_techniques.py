import cv2 as cv
import numpy as np

img= cv.imread('Photos/park.jpg')
cv.imshow('Park', img)


#averaging
average= cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

#guassian blur
gaussian= cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gaussian)


#median blur
median= cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)


#BILATERAL BLUR
#MOST EFFECTIVE BECAUSE IT PRESERVES EDGES
bilateral= cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0) # 0 means infinite time