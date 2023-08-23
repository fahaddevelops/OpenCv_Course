import cv2
import numpy as np

img = cv2.imread("resources/girl.jpg")
# For Gray image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# For image Blur
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
#  For Canny Image
imgCanny = cv2.Canny(imgBlur,100,100)
# For Dilation Image
# import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
imgDilation = cv2.dilate(imgCanny,kernel, iterations=1)
# For Eroded Image
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

# -------------SCALE-----------------

scale = 0.8
img = cv2.resize(img,(0, 0), None, scale, scale)
imgGray = cv2.resize(imgGray,(0, 0), None, scale, scale)
imgBlur = cv2.resize(imgBlur,(0, 0), None, scale, scale)
imgCanny = cv2.resize(imgCanny,(0, 0), None, scale, scale)
imgDilation = cv2.resize(imgDilation,(0, 0), None, scale, scale)
imgEroded = cv2.resize(imgEroded,(0, 0), None, scale, scale)

# convert all images Gray to BGR
imgGray = cv2.cvtColor(imgGray,cv2.COLOR_GRAY2BGR)
imgBlur = cv2.cvtColor(imgBlur,cv2.COLOR_GRAY2BGR)
imgCanny = cv2.cvtColor(imgCanny,cv2.COLOR_GRAY2BGR)
imgDilation = cv2.cvtColor(imgDilation,cv2.COLOR_GRAY2BGR)
imgEroded = cv2.cvtColor(imgEroded,cv2.COLOR_GRAY2BGR)

hor1 = np.hstack((img, imgBlur, imgCanny))
hor2 = np.hstack((imgGray, imgDilation, imgEroded))
ver = np.vstack((hor1, hor2))
new_height = 500  # Choose a common height for both images
new_width = int(new_height * ver.shape[1] / ver.shape[0])
ver = cv2.resize(ver, (new_width, new_height))
cv2.imshow("Ver", ver)
cv2.waitKey(0)
