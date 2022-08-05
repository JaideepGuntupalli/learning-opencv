import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Photos/puppy.jpg')
cv.imshow('Puppy Reference', img)

# plt.imshow(img)
# plt.show()

#BGR to GRAY SCALE
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Puppy',gray)

#BGR to HSV
HSVimg = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV Puppy',HSVimg)

#BGR to L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('Lab Puppy',lab)

#BGR to RGB
RGB_img= cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB Puppy',RGB_img)

plt.imshow(RGB_img)
plt.show()

#
cv.waitKey(0)