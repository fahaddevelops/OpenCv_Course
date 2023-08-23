import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("resources/cards.jpg")
cv2.imshow("cards", img)
plt.imshow(img)
plt.show()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
# BGR to LAB
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)
#bgr to rgb
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("rgb", rgb)

cv2.waitKey(0)
