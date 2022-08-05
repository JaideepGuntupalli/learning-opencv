import cv2 as cv:

def trainer_img(trainerimg):
    ret,thresh=cv.threshold(trainerimg.copy(), 200,255,cv.THRESH_BINARY_INV)

    contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        peri=cv.arcLength(cnt,True)
        area=cv.contourArea(cnt)

    return peri,area

def regular_shape():
    ret,thresh=cv.threshold(img.copy(), 200,255,cv.THRESH_BINARY_INV)

    contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

    peri=cv.arcLength(img,True)

    area=cv.contourArea(contours)

    return peri,area



