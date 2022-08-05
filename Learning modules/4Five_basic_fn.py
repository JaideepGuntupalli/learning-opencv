import cv2 as cv
import numpy as np

img = cv.imread('Photos/puppy.jpg')
cv.imshow('Pupppy',img)

#1.Converting to Grayscale
gray_img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#iT Takes(source, color code conversion)
cv.imshow('Grayscale puppy',gray_img)

#2.Blur # There are many ways to Blur but for now we will use Gaussian blur
blur_img=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
#It takes(sourceimg, Kernel size(its 2x2 tuple which is window size that openCV uses to blur)
# (Ksize has to be an ODD no.),this is border ig, idk )
#To increase the blur we can increase the kernel size
cv.imshow('bLURRED Puppy',blur_img)

#3.Edge Cascade # There are many ways to Edge Cascade but for now we will use the canny edge detector
img1=cv.imread('Photos/flower.jpg')
canny = cv.Canny(img1,125,175)
#Here with canny fn we can find edges
cv.imshow("Canny Edges",canny)

#but sometimes if we get more edges then it can silghtly reduced by blurring the img
blur_img1=cv.GaussianBlur(img1,(3,3),cv.BORDER_DEFAULT)
canny_blur = cv.Canny(blur_img1,125,175)
cv.imshow("Canny Edges blur",canny_blur)

#4.Dilating the image # we do this using the canny edges found above
dilated_img1=cv.dilate(canny,(7,7),iterations=3)
#It takes(src,ksize,iteratons)
cv.imshow("Dilated flower",dilated_img1)
#we can also erode the dilated img to get back canny type img

#5.Eroding # this almost works many times but cant be perfect # basically anti dilating
eroded_img1=cv.erode(dilated_img1,(7,7),iterations=3)
#It takes(src,ksize,iteratons)
cv.imshow("eroded flower",eroded_img1)

#6.Resizing
resize_img1=cv.resize(img1,(500,500),interpolation=cv.INTER_AREA)
#It takes (src,Destination size,interpolation)
#interpolation=cv.INTER_AREA can be used when reducing
#interpolation=cv.INTER_LINEAR or cv.INTER_CUBIC can be used while increasing the size
#cubic slowest but gives high qualtiy
cv.imshow('Resize',resize_img1)

#7.Cropping
#As images are arrays we can select portion of array by array slicing
cropped=img[50:200, 200:400]
cv.imshow('Cropped_img',cropped)

cv.waitKey(0)