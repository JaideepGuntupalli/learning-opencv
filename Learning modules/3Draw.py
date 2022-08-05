#DRAWING SHAPES AND STUFF
import cv2 as cv
import numpy as np
# #We can draw on an img by taking it normally through imread
# img=cv.imread('Photos/flower.jpg')
#For now we will draw on blank image

#Or we can take a blank image
blank = np.zeros((500,500,3), dtype='uint8')#we are making blank img by giving a shape of 
#(height,width,no. of color channels)
#With fn np.zeros() and "dtype" which means data type which was defined as
# "uint8" which means image 
blank1 = np.zeros((500,500,3), dtype='uint8')
blank2 = np.zeros((500,500,3), dtype='uint8')
blank3 = np.zeros((500,500,3), dtype='uint8')
blank4 = np.zeros((500,500,3), dtype='uint8')
blank5 = np.zeros((500,500,3), dtype='uint8')
blank6 = np.zeros((500,500,3), dtype='uint8')
blank7 = np.zeros((500,500,3), dtype='uint8')

cv.imshow('Blank img blank',blank)

#1.Paint The image a certain colour
blank[:] = 255,0,0
#Color pallete: B, G, R 
cv.imshow('Blank img blue',blank)

#2.Coloring certain portion of image by giving a range of pixels
blank1[200:300,300:400]=0,0,255
#range of pixels is given similar to string slicing i.e [start,end,step]
cv.imshow('Blank img red square',blank1)

#3.printing dots
blank2[100:400:10,100:400:10]=0,255,0
##range of pixels is given similar to string slicing i.e [start,end,step]
cv.imshow('dots',blank2)

#4.Draw a rectangle
cv.rectangle(blank3,(0,0),(300,300),(0,255,0), thickness=2)
#here we mention
#(image,point1(with cooardinades in x,y),point2(x2,y2),color,thickness of outline )
cv.imshow("Rectangle",blank3)

#5.Another way of rectangle
cv.rectangle(blank4,(blank4.shape[1]//4,blank4.shape[0]//4),
(3*blank4.shape[1]//4,3*blank4.shape[0]//4),(255,255,0), thickness=cv.FILLED)
#instead of cv.FILLED in thickness we cal also keep -1
cv.imshow('FilledRect',blank4)

#6.Drawing a circle
cv.circle(blank5,(blank5.shape[1]//2,blank5.shape[0]//2),50,(100,100,100),thickness=5)
#here we mention(image,centre(with cooardinades in x,y),radius,color,thickness of circle)
#similarly we can use thickness = cv.FILLED or thickness = -1 to get filled color circle
cv.imshow('circle',blank5)

#7.Draw a Line
cv.line(blank6,(100,100),(400,400),(10,240,175),thickness=2)
#here we mention(image,start(with cooardinades in x,y),end(x2,y2),color,thickness of line)
cv.imshow('Line',blank6)

#Text on image
cv.putText(blank7,"HELLO WORLD,I am here to conquer",(100,250),
cv.FONT_HERSHEY_TRIPLEX,0.5,(255,255,255),thickness=1)
#here we mention(image,Start(x,y),fontFace,,Scale,color,thickness of text)
cv.imshow('text',blank7)

cv.waitKey(0)