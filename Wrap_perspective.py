import cv2
import numpy as np

# Load the image


frameWidth = 700
frameHeight = 500
img = cv2.imread("resources/cards.jpg")
width, height = 250, 350
img = cv2.resize(img, (frameWidth, frameHeight))
pts1 = np.float32([[403,65],[661, 124],[318, 401],[583, 453]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix,(width, height))
print(pts1)
# Convert center coordinates to integers
for x in range(0, 4):
    center = (int(pts1[x][0]), int(pts1[x][1]))
    cv2.circle(img, center, 10, (0, 255, 0), cv2.FILLED)

cv2.imshow("Cards", img)

cv2.imshow("img Cards", imgOutput)
cv2.waitKey(0)  # milliseconds
