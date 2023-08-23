import cv2 
import numpy as np
# ----------FOR IMAGE-------------
# load the image
img = cv2.imread("resources/cat.jpg")

cv2.imshow("cats", img)
imgblank = np.zeros(img.shape[:2], dtype="uint8")
# cv2.imshow("Blank", imgblank)
# ------------mask-----------
mask = cv2.rectangle(imgblank, (imgblank.shape[1]//2 , imgblank.shape[0]//2), (imgblank.shape[1]//2 + 50, imgblank.shape[0]//2 + 100), 200, 255, -1)
# imgblank = cv2.resize(imgblank, (200, 200), None, 0.8, 0.8) 
# cv2.imshow("Masked ", mask)
cir = cv2.circle(imgblank, (imgblank.shape[1]//2 , imgblank.shape[0]//2), 200, 255, -1)
masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("pic", masked)
pic = cv2.bitwise_and(cir, mask)
cv2.imshow("pic", pic)
cv2.waitKey(0) 