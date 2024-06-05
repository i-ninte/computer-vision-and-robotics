'''
in this script we learn how to read images and videos with opencv'''
import cv2 as cv
img= cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat', img)
cv.waitKey(0) # 0 means infinite time