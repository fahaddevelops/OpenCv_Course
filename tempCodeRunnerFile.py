import cv2 
# import numpy as np
import matplotlib.pyplot as plt
# ----------FOR IMAGE-------------
# load the image
img = cv2.imread("resources/cat.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
# cv2.imshow("cats", img)


# -------------- Histogram --------------------
gray_hist = cv2.calcHist([gray], 0, None, [256], [0, 256])
plt.figure()
plt.title("Gray Histogram")
plt.xlabel("Bins")
plt.ylabel('No. of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
cv2.waitKey(0)
plt.show()

cv2.waitKey(0)