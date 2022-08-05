import cv2 as cv
import numpy as np

img = cv.imread('Photos/puppy.jpg')

cv.imshow('Puppy cute',img)

#1.Translation
#Shifting an image across x and y axis
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])#list with 2 lists#Matrix
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
#-x ---> Left
#-y ---> Up
#x ---> Right
#y ---> Down
translated = translate(img,-100,-100)
cv.imshow('Translate_pup',translated)

#2.Rotation
def rotate(img,angle,scale=1.0,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)

    RotMat=cv.getRotationMatrix2D(rotPoint,angle,scale)
    dimensions=(width,height)
    return cv.warpAffine(img,RotMat,dimensions)
#Clockwise --> -ve angle values
#AntiClockwise --> +ve angle values
rotated=rotate(img,45)
cv.imshow('Rotated img',rotated)

#3.Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#4.Fliping
# 0 -->flipping vertically
# 1 -->flipping horizontally
#-1 -->flipping both verically and horizontally
Flipping=cv.flip(img,1)
cv.imshow('flippin',Flipping)

#5.Cropping
cropped=img[200:400,300:500]
cv.imshow('Crop',cropped)


cv.waitKey(0)