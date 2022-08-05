import cv2 as cv
import numpy as np
img=cv.imread('Photos/plates.jpg')
cv.imshow('Plates',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
blank1=np.zeros(img.shape[:2],dtype='uint8')
blank2=np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv.split(img)
cv.imshow('RED',r)
cv.imshow('GREEN',g)
cv.imshow('BLUE',b)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('RED1',red)
cv.imshow('GREEN1',green)
cv.imshow('BLUE1',blue)

final=cv.merge([b,g,r])
cv.imshow('Final mx',final)

efinal=final-(blue)
cv.imshow('d',efinal)


cv.waitKey(0)