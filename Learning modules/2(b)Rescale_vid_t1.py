import cv2 as cv
#this method works for live videos,videos and images.
#Similar method can be used for rescaling images.For example check Rescale_img.py
#rescaleFrame fn is defined such that frame gets multipled with scale
def rescaleFrame(frame, scale=0.75): #here default scale is 0.75
    width = int(frame.shape[1] * scale) #frame.shape[1] gives width of frame
    height = int(frame.shape[0] * scale) #frame.shape[0] gives height of frame
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA) #cv.resize resizes the frame to given dimensions

'''Reading Videos'''

capture = cv.VideoCapture('Videos/Sample_1.mp4')#cpature is a variable
#we are reading videos by giving address with VideoCapture() fn frame by frame
#we can also use (0) instead of ('address') to get a webcam

while True:
    isTrue, frame = capture.read() #frame is variable
    #capture.read() reads the given video frame by frame
    #isTrue is a bool fn which says whether reading was succesful or not 
    
    frame_resized=rescaleFrame(frame,0.2)#calling defined fn to resize the frame
    
    cv.imshow('Video',frame) #this is showing video frame by frame
   #'video' or 'video rezied is just name of the window it appears in
    cv.imshow('Video Resized', frame_resized) #this is showing resized vid frame by frame

    if cv.waitKey(20) & 0xFF==ord('d'): #here 0xFF==ord('d') means on pressing d will give true
        break #this loop is to stop playing it indefinetely

capture.release() #to release the capture pointer
cv.destroyAllWindows() #to destroy all windows
