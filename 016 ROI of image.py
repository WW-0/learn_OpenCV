import cv2
import numpy as np

image0 = cv2.imread('01a.jpg')
cv2.namedWindow('image0', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image0', image0)
h, w = image0.shape[:2]

# 获取ROI  region of interest，感兴趣区域。
cy = h // 2  # /自动浮点型除法，//自动整形除法
cx = w // 2
roi = image0[cy - 100:cy + 100, cx - 100:cx + 100, :]  # [x1:x2,:]  x=x1到x2，y=全体y
cv2.imshow('roi', roi)

# copy ROI
image1 = np.copy(roi)  # 浅复制，对第一层无影响，深层有影响如列表中的列表

# modify ROI  修改更改
roi[:, :, 1] = 0
cv2.imshow('result0', roi)
cv2.imshow('result1', image0)  # 赋值的影响，修改roi会影响image0

# modify copy roi
image1[:, :, 2] = 0  # 浅复制，修改image1不会影响roi
cv2.imshow("result2", image0)
cv2.imshow("result3", roi)
cv2.imshow("copy roi", image1)

# example with ROI - generate mask  生成掩膜
image2 = cv2.imread('01a.jpg')
hsv = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (33, 43, 46), (99, 255, 255))
# 将低于lower和高于upper的部分分别变成0，lower～upper之间的值变成255

# extract person ROI  提取目标
mask = cv2.bitwise_not(mask)
cv2.imshow('mask1', mask)
person = cv2.bitwise_and(image2, image2, mask=mask)  # 原图和原图进行 与 运算无任何影响，主要是想进行掩膜运算
cv2.imshow('person', person)

# generate background
result = np.zeros(image2.shape, image2.dtype)
result[:, :, 0] = 255

# combine background + person
mask = cv2.bitwise_not(mask)
cv2.imshow('mask2', mask)
dst = cv2.bitwise_or(person, result, mask=mask)  # 先把整个图染成蓝色B，在用掩膜提取目标物
cv2.imshow("dst1", dst)
dst = cv2.add(dst, person)
cv2.imshow("dst2", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
