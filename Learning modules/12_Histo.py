import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Photos/car.png')
cv.imshow('ORIFINaL',img)

gray_car=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Graycar',gray_car)

#Grayscale histogram
gray_hist=cv.calcHist([gray_car], [0], None, [256], [0,256] )

plt.figure()
plt.title('Grayscale Histogram')#title giving
plt.xlabel('Bins')#x label
plt.ylabel('# of pixels')#y label
plt.plot(gray_hist)# plotting it
plt.xlim([0,256])#giving limit in x axis
plt.show()

cv.waitKey(0)