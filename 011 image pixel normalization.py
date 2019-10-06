# normalization 标准化 常规化
import cv2
import numpy as np

image0 = cv2.imread('01a.jpg')
cv2.namedWindow('input', cv2.WINDOW_FREERATIO)
cv2.imshow('input', image0)
gray = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# 转为浮点数类型数组
gray = np.float32(gray)
print(gray)

# scale and shift by NORM_MINMAX
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv2.NORM_MINMAX)
# 归一化函数，gray输入矩阵，dst输出矩阵，alpha最小值，beta最大值，norm_type归一化类型
print(dst)
print(np.uint8(dst * 255))
cv2.imshow('NORM_MINMAX', np.uint8(dst * 255))  # 归一化之后数据太小显示不明显

# scale and shift by NORM_INF
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_INF)
print(dst)
print(np.uint8(dst * 255))
cv2.imshow("NORM_INF", np.uint8(dst * 255))

# scale and shift by NORM_L1
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_L1)
print(dst)
print(np.uint8(dst * 10000000))
cv2.imshow("NORM_L1", np.uint8(dst * 10000000))

# scale and shift by NORM_L2
dst = np.zeros(gray.shape, dtype=np.float32)
cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_L2)
print(dst)
print(np.uint8(dst * 10000000))
cv2.imshow("NORM_L2", np.uint8(dst * 10000))

cv2.waitKey(0)
cv2.destroyAllWindows()
