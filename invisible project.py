import cv2
import numpy as np

def free(a):
    pass

# initialize the camera
cap = cv2.VideoCapture(0)
bars = cv2.namedWindow("bars")

cv2.createTrackbar("upper_hue", "bars", 110, 180, free)
cv2.createTrackbar("upper_sat", "bars", 255, 255, free)
cv2.createTrackbar("upper_val", "bars", 255, 255, free)
cv2.createTrackbar("lower_hue", "bars", 68, 180, free)
cv2.createTrackbar("lower_sat", "bars", 55, 255, free)
cv2.createTrackbar("lower_val", "bars", 54, 255, free)

while True:
    cv2.waitKey(1000)
    ret, init_frame = cap.read()
    if ret:
        break

# Start capturing the frames for actual magic
while True:
    ret, frame = cap.read()
    inspect = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    upper_hue = cv2.getTrackbarPos("upper_hue", "bars")
    upper_sat = cv2.getTrackbarPos("upper_sat", "bars")
    upper_val = cv2.getTrackbarPos("upper_val", "bars")
    lower_hue = cv2.getTrackbarPos("lower_hue", "bars")
    lower_sat = cv2.getTrackbarPos("lower_sat", "bars")
    lower_val = cv2.getTrackbarPos("lower_val", "bars")

    # Kernel for dilation
    kernel = np.ones((3, 3), np.uint8)

    U = np.array([upper_hue, upper_sat, upper_val])
    L = np.array([lower_hue, lower_sat, lower_val])

    mask = cv2.inRange(inspect, L, U)
    mask = cv2.medianBlur(mask, 3)
    mask_inv = 255 - mask
    mask = cv2.dilate(mask, kernel, 5)

    # the mixing of frames in a combination to achieve the req frame
    b = frame[:, :, 0]
    g = frame[:, :, 1]
    r = frame[:, :, 2]
    b = cv2.bitwise_and(mask_inv, b)
    g = cv2.bitwise_and(mask_inv, g)
    r = cv2.bitwise_and(mask_inv, r)
    frame_inv = cv2.merge((b, g, r))

    b = frame[:, :, 0]
    g = frame[:, :, 1]
    r = frame[:, :, 2]
    b = cv2.bitwise_and(b, mask)
    g = cv2.bitwise_and(g, mask)
    r = cv2.bitwise_and(r, mask)
    blanket_area = cv2.merge((b, g, r))

    final = cv2.bitwise_or(frame_inv, blanket_area)
    cv2.imshow("Harry's Cloak", final)
    cv2.imshow("original", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
