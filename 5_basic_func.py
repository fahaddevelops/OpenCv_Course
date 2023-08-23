import cv2
# ----------FOR IMAGE-------------
# load the image
img = cv2.imread("resources/girl.jpg")
# For Gray image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# For image Blur
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
#  For Canny Image
imgCanny = cv2.Canny(imgBlur,100,100)
# For Dilation Image
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
imgDilation = cv2.dilate(imgCanny,kernel, iterations=1)
# For Eroded Image
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("girl", img)
cv2.imshow("GrayScale", imgGray)
cv2.imshow("Img Blur", imgBlur)
cv2.imshow("Img Canny", imgCanny)
cv2.imshow("Img Dilation", imgDilation)
cv2.imshow("Img Erode", imgEroded)
cv2.waitKey(0)