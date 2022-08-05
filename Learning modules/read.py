import cv2 as cv
import matplotlib.pyplot as plt



img = cv.imread('Photos/flower.jpg')
# cv.imshow('Puppy cute',img)

# print(img.shape)
# plt.imshow(img,cmap='gray',)
# plt.show=('img',img)
# print(img.shape[:2])
plt.imshow(img)
plt.show()

cv.waitKey(0)
