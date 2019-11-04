# 经过高斯运算的叫LOG，没有经过高斯的叫原始拉普拉斯算子
import cv2 as cv
import numpy as np

image = cv.imread("01a.jpg", 0)
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", image)

h, w = image.shape[:2]
src = cv.GaussianBlur(image, (0, 0), 1)
dst = cv.Laplacian(src, cv.CV_32F, ksize=3, delta=10)  # delta增加边缘亮度
dst = cv.convertScaleAbs(dst)  # 该函数对每个元素进行三步操作：缩放、绝对值、转换为无符号8位
result = np.zeros([h, w * 2], dtype=image.dtype)
result[0:h, 0:w] = image
result[0:h, w:2 * w] = dst
cv.imshow("result", result)

dst1 = cv.Laplacian(image, cv.CV_32F, ksize=3)  # 对比不滤波
dst1 = cv.convertScaleAbs(dst1)
cv.imshow("result1", dst1)

cv.waitKey(0)
cv.destroyAllWindows()
