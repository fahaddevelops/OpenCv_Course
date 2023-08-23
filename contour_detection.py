import cv2
import numpy as np

img = cv2.imread("resources/girl.jpg")
# cv2.imshow("img", img)
imgBlank = np.zeros(img.shape, dtype="uint8") 
# cv2.imshow("Blank",imgBlank)
# For Gray image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("imgs", imgGray)
# For image Blur
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# cv2.imshow("Blur", imgBlur)
# #  For Canny Image
imgCanny = cv2.Canny(imgBlur,125,175)
cv2.imshow("Canny",imgCanny) 

ret, thresh= cv2.threshold(imgGray, 125, 125, cv2.THRESH_BINARY)
cv2.imshow("Thresh", thresh)

contours, hierarcies = cv2.findContours(imgCanny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')
# Draw contours
cv2.drawContours(imgBlank, contours, -1, (0,0,255),1)
cv2.imshow("Contours", imgBlank)
cv2.waitKey(0)
