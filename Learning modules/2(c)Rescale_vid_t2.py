import cv2 as cv
#This method is specifically for live videos only
#DISCLAIMER:".set()" fn |i dont know| need to clarify|
def changeRes(width,height):
    capture.set(10,width)
    capture.set(4,height)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    w=frame.shape[1]
    h=frame.shape[0]
    frame_resized=changeRes(w,h)
    cv.imshow('LivVid',frame)
    cv.imshow('LivVid Res',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release() #to release the capture pointer
cv.destroyAllWindows() #to destroy all windows

