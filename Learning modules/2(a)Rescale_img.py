import cv2 as cv
#for explaination of defined fn check rescale_vid.py
def rescaleImage(image, scale=0.75):
    height=int(image.shape[0]*scale)
    width=int(image.shape[1]*scale)
    dimensions=(width,height)

    return cv.resize(image,dimensions,interpolation=cv.INTER_AREA)

img = cv.imread('Photos/puppy.jpg') #img is a variable
#we are reading image by giving address with imread() fn
#If the size of image is way bigger than the size of monitor it goes out of the window
resized_img=rescaleImage(img)

cv.imshow('puppy', img) #we are printing image with imshow() fn
cv.imshow('resized puppy', resized_img) #we are printing resized image

cv.waitKey(0) #for now don't care