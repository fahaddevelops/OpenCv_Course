import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
    imgCanny = cv2.Canny(imgBlur, 100, 100)
    imgBlank = np.zeros((480, 480), np.uint8)

    kernel = np.ones((5, 5), np.uint8)

    imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
    # imgDilation.shape
    imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

    hor1 = np.hstack((imgBlur, imgCanny, imgBlank))
    hor2 = np.hstack((imgDilation, imgEroded, imgBlank))

    ver = np.vstack((hor1, hor2))

    # Resize vertically stacked image
    new_height = 500
    new_width = int(new_height * ver.shape[1] / ver.shape[0])
    ver = cv2.resize(ver, (new_width, new_height))

    cv2.imshow("Ver", ver)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



