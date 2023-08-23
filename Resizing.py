import cv2
import numpy as np

def resizer(frame, scale= 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv2.resize(frame, dimensions, interpolation= cv2.INTER_AREA)

cap = cv2.VideoCapture(0)
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)
while True:
    sucess,img = cap.read()
    img_resize = resizer(img)
    cv2.imshow("road", img)
    cv2.imshow("road_sized", img_resize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    