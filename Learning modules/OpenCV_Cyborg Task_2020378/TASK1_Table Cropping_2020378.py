#TASK 1: Crop all the tables from the image provided to you using OpenCV
#DONE by Jaideep Guntupalli|CSD|2020378

#Imported cv
import cv2 as cv

#Defining fn to rescale any image if required
def rescaleImage(image, scale=0.3):
    scale_given=scale
    height=int(image.shape[0]*scale)
    width=int(image.shape[1]*scale)
    dimensions=(width,height)
    return cv.resize(image,dimensions,interpolation=cv.INTER_AREA),scale_given

#Taking input from user about address of image
img_address=input("Please Enter the address of the image : ")

#Reading the image
img_org = cv.imread(img_address)

#Rescaling if needed
img_rescaled,scale=rescaleImage(img_org)

#GrayScaling for better results
img_gray=cv.cvtColor(img_rescaled,cv.COLOR_BGR2GRAY)

#Defining a fn to identify table coordinates
def identify_table(img):
    #Inverse binary threshold to increase clarity of required pixels
    ret,thresh=cv.threshold(img.copy(), 200,255,cv.THRESH_BINARY_INV)

    #Finding Contours to get coordinates
    contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

    #Appending a list of whose contours are big enough to be a table
    coordinates_list=[]
    for cnt in contours:
        x,y,w,h = cv.boundingRect(cnt)
        if w>(img.shape[0])//2:
            coordinates_list.append((x,y,x+w,y+h))
    
    return coordinates_list

#Finding coordinates of the tables in given image
coordinates=identify_table(img_gray)

#Defing a fn to crop tables from given coordinates
def crop_table(index,lst):
    index_lst=lst[index]
    table_no=i+1
    window_name='Table '+ str(table_no)#Custom names for every window
    #Cropping img # Added and subtracted 5 pixels for aesthetics
    #rescaling pixel values to crop from orginal image for better quality
    wid1=int((index_lst[1]//scale)-5)
    wid2=int((index_lst[3]//scale)+5)
    hgt1=int((index_lst[0]//scale)-5)
    hgt2=int((index_lst[2]//scale)+5)
    cropped_img=img_org[wid1:wid2,hgt1:hgt2]
    cv.imshow(window_name,cropped_img)

#Appling for loop to show all tables
for i in range(len(coordinates)):
    crop_table(i,coordinates)

cv.waitKey(0)