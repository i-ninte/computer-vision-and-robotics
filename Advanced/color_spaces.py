import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img= cv.imread('Photos/Cat.jpg')
cv.imshow('Cat', img)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.show()
#convert to grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#convert to hsv
hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#convert to rgb
rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#convert to L*a*b
Lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab', Lab)


cv.waitKey(0) # 0 means infinite time
