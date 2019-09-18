import cv2
import numpy as np

image1 = cv2.imread('01.jpg')
cv2.namedWindow('image1', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image1', image1)

"""clone image"""
image2 = np.copy(image1)
cv2.imshow('image2', image2)

"""assign 赋值"""
image3 = image2  # 参看浅赋值和深复制
image2[100:200, 200:300, :] = 255
cv2.imshow('image3', image3)

image4 = np.zeros(image1.shape, image1.dtype)
cv2.imshow('image4', image4)

image5 = np.zeros([512, 512], np.uint8)  # 创建的是二维零矩阵
cv2.imshow('image5', image5)

image6 = np.zeros([512, 512, 3], np.uint8)  # 创建三维零矩阵
image6[:, :, 2] = 255
cv2.imshow('image6', image6)

image7 = np.ones(shape=[512, 512, 3], dtype=np.uint8)
image7[:, :, 1] = 255
cv2.imshow('image7', image7)

cv2.waitKey(0)
cv2.destroyAllWindows()
