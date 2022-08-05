import cv2 as cv

'''Reading Videos'''

capture = cv.VideoCapture('Videos/Sample_1.mp4')#cpature is a variable
#we are reading videos by giving address with VideoCapture() fn frame by frame
#we can also use (0) instead of ('address') to get a webcam

while True:
    isTrue, frame = capture.read() #frame is variable
    #capture.read() reads the given video frame by frame
    #isTrue is a bool fn which says whether reading was succesful or not 
    cv.imshow('Video', frame)#this is showing frame by frame

    if cv.waitKey(20) & 0xFF==ord('d'):
        break #this loop is to stop playing it indefinetely

capture.release() #to release the capture pointer
cv.destroyAllWindows() #to destroy all windows

#Error>>-215:Assertion failed==Its means open cv cant find media at specified location
#this occurs here when video completes because it ran out of frames to read