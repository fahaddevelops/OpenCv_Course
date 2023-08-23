import cv2
import numpy as np

img = cv2.imread("resources/cat.jpg")
# cv2.imshow("img", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# simple thresholding
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY) # black the Background (Black&White img)
cv2.imshow("Simple threshold", thresh)

threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)# white the background(Black&White img)
cv2.imshow("Simple threshold", thresh)

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
cv2.imshow("Adaptive Threshold", adaptive_thresh)
cv2.waitKey(0)