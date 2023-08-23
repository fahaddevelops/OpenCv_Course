import cv2
import numpy as np

img = cv2.imread("resources/girl.jpg")

cv2.imshow("girl", img)

# --------------------TRANSLATE----------------------------
def trans(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

# -x -> up
# -y -> left
# x -> down
# y -> right

translation = trans(img, -50, 50)
# cv2.imshow("translated", translation)

# -----------------RPTATION
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)
    
    return cv2.warpAffine(img, rotMat, dimension)

# --------------------ROTATE----------------------------
rotation = rotate(img, -45)
# cv2.imshow("Rotated", rotation)

rotations = rotate(img, 90)
# cv2.imshow("Rotated-", rotations)

# --------------------RESIZE----------------------------
resize = cv2.resize(img, (500, 500), interpolation= cv2.INTER_CUBIC)
# cv2.imshow("Resize", resize)

# --------------------FLIP----------------------------
flip = cv2.flip(resize, 1)
cv2.imshow("Fliped", flip)

# --------------------CROP----------------------------
crop = resize[0:400, 300:400]
cv2.imshow("cropped", crop)
cv2.waitKey(0)