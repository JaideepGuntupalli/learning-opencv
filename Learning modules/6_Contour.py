import cv2 as cv
import numpy as np

img = cv.imread('Photos/puppy.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('G',gray)

blank = np.zeros(img.shape,'uint8')

blur=cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

canny = cv.Canny(blur,125,175)
cv.imshow("Canny edgse",canny)

# ANOTHER METHOD:
# ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)


contours,heirarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
#THE above fn gives two values #Contours is essentially a python list of all coordinates 
#Hierarchies is representation used by OpenCV to find contours

#MODE:
#RETR_TREE ----->All Hierarchial Contours
#RETR_EXTERNAL ->Only External Contours
#RETR_LIST ----->All Contours in IMG

#METHOD:
#CHAIN_APPROX_NONE ---> All without any approx
#CHAIN_APPROX_SIMPLE -> With compressed VAlues making in simple

cv.drawContours(blank,contours,-1,(0,255,1),1)
cv.imshow('Conmtoues,fn',blank)


print(len(contours))
print(contours)

cv.waitKey(0)