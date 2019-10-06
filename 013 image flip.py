import cv2
import numpy as np

image0 = cv2.imread('01a.jpg')
cv2.namedWindow('image0', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image0', image0)

# X Flip 倒影
image1 = cv2.flip(image0, 0)
cv2.imshow('x-flip', image1)

# Y Flip 镜像
image2 = cv2.flip(image0, 1)
cv2.imshow('y-flip', image2)

# XY Flip 对角
image3 = cv2.flip(image0, -1)
cv2.imshow("xy-flip", image3)

# custom x-flip  自定义翻转
h, w, ch = image0.shape
image5 = np.zeros(image0.shape, dtype=image0.dtype)
for row in range(h):
    for col in range(w):
        b, g, r = image0[row, col]
        image5[h - row - 1, col] = [b, g, r]
cv2.imshow('custom x-flip', image5)

# custom y-flip  自定义翻转
h, w, ch = image0.shape
image4 = np.zeros(image0.shape, dtype=image0.dtype)
for row in range(h):
    for col in range(w):
        b, g, r = image0[row, col]
        image4[row, w - col - 1] = [b, g, r]
cv2.imshow("custom-y-flip", image4)

cv2.waitKey(0)
cv2.destroyAllWindows()
