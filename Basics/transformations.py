import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# Translations
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotations
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0)
cv.imshow('Flipped', flip)

# Wait for a key event indefinitely or for a delay of specified milliseconds
cv.waitKey(0) # 0 means infinite time
