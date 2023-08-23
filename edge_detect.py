import cv2
import numpy as np

img = cv2.imread("resources/buildings.jpg")
cv2.imshow("img", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# laplacian
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

# sobel

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
# now combine X & Y
combine_sobel = cv2.bitwise_and(sobelx, sobely)
cv2.imshow("X", sobelx)
cv2.imshow("Y", sobely)
cv2.imshow("X|Y", combine_sobel)

cv2.imshow('LAP', lap)
cv2.waitKey(0)