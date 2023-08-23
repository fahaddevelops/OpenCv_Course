import cv2
import numpy as np

circles = np.zeros((4, 2))
counter = 0

def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter += 1
        print(circles)
        # if counter >= 4:
        #     counter = 0  # Reset counter after processing points

img = cv2.imread("resources/cards.jpg")
frameWidth = 700
frameHeight = 500

while True:
    if counter == 4:
        width, height = 250, 350
        img = cv2.resize(img, (frameWidth, frameHeight))
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("img book", imgOutput)
    for x in range(0, 4):
        center = (int(circles[x][0]), int(circles[x][1]))
        cv2.circle(img, center, 3, (0, 255, 0), cv2.FILLED)

    cv2.imshow("book", img)
    cv2.setMouseCallback("book", mousePoints)
    cv2.waitKey(1)  # milliseconds
