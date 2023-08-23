import cv2
import numpy as np

# create a blank image
imgBlank = np.zeros((400, 400, 3), dtype="uint8")

rectangle = cv2.rectangle(imgBlank.copy(), (30,30), (370,370),255,-1)
circle = cv2.circle(imgBlank.copy(), (200,200), 200,255,-1)

cv2.imshow('Rectangle', rectangle)
cv2.imshow('circle', circle)

# bitwise Opreator (AND)
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow("Bitwise", bitwise_and)

# bitwise Opreator (OR)
bitwise_or = cv2.bitwise_or(circle, rectangle)
cv2.imshow("Bitwise", bitwise_or)

# bitwise Opreator (XOR)
bitwise_not = cv2.bitwise_not(circle, rectangle)
cv2.imshow("Bitwise", bitwise_not)

# bitwise Opreator (not)


cv2.waitKey(0)

