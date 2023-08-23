import cv2
import numpy as np

img = cv2.imread("resources/girl.jpg")

img = cv2.resize(img, (500,500),None, 0.5, 0.5)
cv2.imshow("girl", img)
blank = np.zeros(img.shape[:2], dtype="uint8")
b,g,r = cv2.split(img)
blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])
cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
cv2.imshow("Red", red)
# ---------MERGED__IMAGE---------
merged = cv2.merge([b,g,r])
cv2.imshow("m", merged)

print(img.shape)
print(b.shape)
print(g.shape)
cv2.waitKey(0)