import cv2
import numpy as np

image0=cv2.imread('01a.jpg')
# image0 = np.zeros(shape=[400, 400, 3], dtype=np.uint8)
# image0[:, :, 0] = 255
# image0[:, :, 1] = 255
# image0[:, :, 2] = 255
cv2.namedWindow('image0', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image0', image0)

# # 蓝色通道为零
mv = cv2.split(image0)
mv[0][:, :] = 0
#mv[2][:, :] = 0
dst1 = cv2.merge(mv)
cv2.imshow('dst1', dst1)

# # 绿色通道为零
mv = cv2.split(image0)
mv[1][:, :] = 0
dst2 = cv2.merge(mv)
cv2.imshow('dst2', dst2)

# # 红色通道为零
mv = cv2.split(image0)
mv[2][:, :] = 0
dst3 = cv2.merge(mv)
cv2.imshow('dst3', dst3)

cv2.mixChannels([dst1],[dst3],[0,0])  #一定注意输入和输出外层的括号
cv2.imshow('image1',dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()

