import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def empty(a): 
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 23, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 20, 255, empty)

def getContours(img, imgcontour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(imgcontour, contours, -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgcontour, (x, y), (x + w, y + h), (0, 255, 0), 5)

while True:
    success, img = cap.read()
    imgcontour = img.copy()
    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    getContours(imgDil, imgcontour)

    # Resize images to have the same number of rows
    min_rows = min(imgBlur.shape[0], imgCanny.shape[0], imgDil.shape[0], imgcontour.shape[0])
    imgBlur = imgBlur[:min_rows]
    imgCanny = imgCanny[:min_rows]
    imgDil = imgDil[:min_rows]
    imgcontour = imgcontour[:min_rows]

    # Convert contour image to grayscale
    imgContourGray = cv2.cvtColor(imgcontour, cv2.COLOR_BGR2GRAY)

    # Stack horizontally
    hor1 = np.hstack([imgBlur, imgCanny])
    hor2 = np.hstack([imgDil, imgContourGray])

    # Stack vertically
    ver = np.vstack([hor1, hor2])
    cv2.imshow("Vertical stack", ver)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
