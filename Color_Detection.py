import cv2
import numpy as np

# WE are going to use hsv color space
frameWidth = 300
frameHeight = 350

cap = cv2.VideoCapture(0)
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)
def empty(a): 
    pass
cv2.namedWindow('HSV')
cv2.resizeWindow('HSV', 300, 350)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)
while True:
    success, img = cap.read()
# hue is Color , Saturation is how pure the color and value is how bright the color
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min","HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    print(h_min)

    # now we crete a mask and Results
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    results = cv2.bitwise_and(img, img, mask = mask)

    img = cv2.resize(img,(frameWidth,frameHeight))
    mask = cv2.resize(mask, (300, 350))  # Adjust mask size
    results = cv2.resize(results, (300, 350))
    #  Now we take Images togather
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hor1 = np.hstack([img, mask, results])
    cv2.imshow("Horizontal Stack", hor1)
    # cv2.imshow("Web cam", img)
    # # cv2.imshow("webcam", imgHsv)
    # # Show mask and Result
    # cv2.imshow("MASK", mask)
    # cv2.imshow("Result", results)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break