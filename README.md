
## OpenCV Course

Welcome to the OpenCV course! This repository is a comprehensive guide to learning OpenCV, covering various topics and techniques for image and video processing.

### Table of Contents

1. [Introduction to OpenCV](#introduction-to-opencv)
2. [Reading and Displaying Images and Videos](#reading-and-displaying-images-and-videos)
3. [Basic Image Operations](#basic-image-operations)
   - Grayscale Conversion
   - Blurring
   - Canny Edge Detection
   - Dilation and Erosion
4. [Image Composition and Manipulation](#image-composition-and-manipulation)
   - Combining Images
   - Drawing Shapes and Text
   - Bitwise Operators
5. [Histogram Analysis](#histogram-analysis)
6. [Image Splitting and Merging](#image-splitting-and-merging)
7. [Image Transformation and Rotation](#image-transformation-and-rotation)
8. [Image Masking](#image-masking)
9. [Laplacian and Sobel Operators](#laplacian-and-sobel-operators)
10. [... (Add more topics)](#add-more-topics)

---

### Introduction to OpenCV

OpenCV (Open Source Computer Vision Library) is a powerful open-source library that provides various tools for computer vision and image processing applications.

### Reading and Displaying Images and Videos

#### Reading Images

```python
import cv2

# Read an image
image = cv2.imread('image.jpg')

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

#### Reading Videos

```python
import cv2

# Open a video capture
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Basic Image Operations

#### Grayscale Conversion

```python
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

#### Blurring

```python
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

#### Canny Edge Detection

```python
edges = cv2.Canny(image, threshold1, threshold2)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

#### Dilation and Erosion

```python
kernel = np.ones((5, 5), np.uint8)
dilated_image = cv2.dilate(image, kernel, iterations=1)
eroded_image = cv2.erode(image, kernel, iterations=1)
```

### Image Composition and Manipulation

#### Combining Images

```python
combined_image = cv2.addWeighted(image1, alpha, image2, beta, gamma)
```

#### Drawing Shapes and Text

```python
cv2.line(image, start_point, end_point, color, thickness)
cv2.rectangle(image, top_left, bottom_right, color, thickness)
cv2.circle(image, center, radius, color, thickness)
cv2.putText(image, text, position, font, font_scale, color, thickness)
```

#### Bitwise Operators

```python
bitwise_and = cv2.bitwise_and(image1, image2, mask=mask)
bitwise_or = cv2.bitwise_or(image1, image2, mask=mask)
bitwise_xor = cv2.bitwise_xor(image1, image2, mask=mask)
bitwise_not = cv2.bitwise_not(image, mask=mask)
```

### Histogram Analysis

```python
histogram = cv2.calcHist([image], channels, mask, hist_size, ranges)
plt.plot(histogram)
```

### Image Splitting and Merging

```python
b, g, r = cv2.split(image)
merged_image = cv2.merge((b, g, r))
```

### Image Transformation and Rotation

```python
M = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, M, (width, height))
```

### Image Masking

```python
mask = np.zeros(image.shape, dtype=np.uint8)
cv2.circle(mask, center, radius, color, -1)
masked_image = cv2.bitwise_and(image, mask)
```

### Laplacian and Sobel Operators

```python
laplacian_image = cv2.Laplacian(gray_image, cv2.CV_64F)
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
```
