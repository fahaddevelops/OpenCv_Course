import cv2
import numpy as np

# create a blank image
imgBlank = np.zeros((500, 500, 3), dtype="uint8")
# # (height, width, channels) = (500, 500, 3)
# ------------- paint an image----------------
imgBlank[:] = (0,255,0)
cv2.imshow("Green", imgBlank)
# # -----------------------Draw A rectangle---------------------------

cv2.rectangle(imgBlank, (0,0), (250,350), (0,0,255), thickness = cv2.FILLED)
#pts1 = origin and thickness= 4 and thickness = cv2.FILLED
cv2.imshow("Rectangle", imgBlank)

# -----------------------Draw A Circle---------------------------

cv2.circle(imgBlank, ((imgBlank.shape[1]//2), (imgBlank.shape[0]//2)), 50, (0,0,0), thickness = -1)
cv2.imshow("Circle", imgBlank)

# -----------------------Draw A Line---------------------------
cv2.line(imgBlank, (0,0), ((imgBlank.shape[1]//2), (imgBlank.shape[0]//2)), (255,255,255), thickness= 5)
cv2.imshow("Line", imgBlank)

# -----------------------Write a text ---------------------------

cv2.putText(imgBlank, "Hi, Fahad", (0,255), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,255), thickness= 2)
cv2.imshow("Text", imgBlank)
cv2.waitKey(0) 