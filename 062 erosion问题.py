import cv2
import numpy as np

# src = cv2.imread("01a.jpg",0)
# 使用3x3结构元素进行膨胀与腐蚀操作
#se = np.ones((2, 2), dtype=np.uint8)
# print(src.dtype)
# print(src.shape)
se = np.array([[1,1],[1,1]], dtype=np.uint8)
print(se,se.shape,se.dtype)
se1 = np.array([[1,0],[1,1]], dtype=np.uint8)
print(se1,se1.shape,se1.dtype)
src = np.array([[0,1,1,0,1,0,0],
                [1,1,1,1,1,1,1],
                [1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1],
                [1,1,1,1,1,0,1],
                [1,0,0,1,1,1,1]],dtype=np.uint8)
print(src)
erode = cv2.erode(src, se,anchor=(0,0))
print(erode)
erode1 = cv2.erode(src, se1,anchor=(0,0))
print(erode1)
#cv2.imshow("erode", erode)
cv2.waitKey(0)
cv2.destroyAllWindows()