import cv2

img = cv2.imread("resources/cat.jpg")


img = cv2.resize(img, (500, 500), None, 0.5, 0.5)
cv2.imshow("cat", img)

# Averaging
average = cv2.blur(img, (7, 7)) #(3, 3)kernel size
cv2.imshow("Ave", average)

#Gaussian Blur
G = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("gb", G)

# Median Blur
med = cv2.medianBlur(img, 7)

#
bilateral = cv2.bilateralFilter(img, 10, 15, 15)
cv2.imshow("Bilateral", bilateral)

cv2.waitKey(0)