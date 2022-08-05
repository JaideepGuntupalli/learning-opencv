#TASK 2 : Extract and count yellow objects from the image (The count should be printed)
#DONE by Jaideep Guntupalli|CSD|2020378

#Imported cv & numpy
import cv2 as cv
import numpy as np

#Defing function to find yellow objects
def yellow_object_finder(image):
    # Converting given image to HSV
    hsv_img = cv.cvtColor(image, cv.COLOR_RGB2HSV)
        
    # Setting yellow range
    light_yellow = (84,73,79)
    dark_yellow  =(104,255,255)

    # Making a yellow mask
    yellow_mask = cv.inRange(hsv_img, light_yellow, dark_yellow)

    contours,hierarchies=cv.findContours(yellow_mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    imp_contours=[]
    for i in contours:
        peri=cv.arcLength(i,True)
        if peri>29:
            imp_contours.append(i)

    blank=np.zeros(yellow_mask.shape,'uint8')

    final_mask=cv.drawContours(blank,imp_contours,-1,(255,255,255),-1)
    
    #Extraxting the yellow objects
    resulting_img = cv.bitwise_and(image, image, mask=final_mask)
    
    #finding total no. of yellow objects
    no_of_yellow_objects=len(imp_contours)
    
    return resulting_img, no_of_yellow_objects

#Taking image as an input from user
img_address=input("Please Enter the address of the image : ")
img = cv.imread(img_address)

#appending the values returned by function to new variables
yellow_object_img,yellow_objects_num = yellow_object_finder(img)


print("Number of yellow objects in the given image are",yellow_objects_num)

cv.imshow('Yellow objects',yellow_object_img)


cv.waitKey(0)