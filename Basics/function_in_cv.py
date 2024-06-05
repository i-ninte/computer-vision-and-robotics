import cv2 as cv
img= cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)



#grayscale image
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)



#blur image
blur= cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#edge cascade
canny= cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)
#dilate image
dilated= cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#resize
resized= cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#cropping
cropped= img[50:200, 200:400]
cv.imshow('Cropped', cropped)




cv.waitKey(0) # 0 means infinite time