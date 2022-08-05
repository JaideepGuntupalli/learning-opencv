import cv2 as cv

img = cv.imread('Photos/puppy.jpg',1) #img is a variable #1:Color 0:grayscale#if not mentioned taken as 1
#we are reading image by giving address with imread() fn
##If the size of image is way bigger than the size of monitor it goes out of the window

cv.imshow('puppy', img) #we are printing image with imshow() fn

cv.waitKey(0) #for now don't care