import cv2
# ----------FOR IMAGE-------------
# load the image
# img = cv2.imread("resources/girl.jpg")
#
# cv2.imshow("girl", img)
# cv2.waitKey(0)  # milliseconds

# ---------------FOR VIDEO----------------

frameWidth = 640
frameHeight = 100

cap = cv2.VideoCapture("resources/road.mp4")
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)
while True:
    sucess,img = cap.read()
    img = cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("road", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break