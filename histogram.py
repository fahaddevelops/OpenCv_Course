import cv2 
# # import numpy as np
# import matplotlib.pyplot as plt
# # ----------FOR IMAGE-------------
# # load the image
# img = cv2.imread("resources/cat.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray)
# # cv2.imshow("cats", img)


# # -------------- Histogram --------------------
# gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
# plt.figure()
# plt.title("Gray Histogram")
# plt.xlabel("Bins")
# plt.ylabel('No. of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# cv2.waitKey(0)
# plt.show()

# cv2.waitKey(0)
import matplotlib.pyplot as plt


# Load the image
img = cv2.imread("resources/girl.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate the histogram
gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Display the histogram
plt.figure()
# plt.title("Gray Histogram")
plt.title("Colour Histogram")
plt.xlabel("Bins")
plt.ylabel('No. of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()    
cv2.waitKey(0)
cv2.destroyAllWindows()
