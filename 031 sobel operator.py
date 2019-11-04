import cv2 as cv
import numpy as np

src = cv.imread("01a.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

h, w = src.shape[:2]
x_grad = cv.Sobel(src, cv.CV_32F, 1, 0)  # 先用32位放着溢出
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)

x_grad = cv.convertScaleAbs(x_grad)  # 因为右侧像素减去左边像素，存在负值的情况，因此使用cv2.convertScalerAbs() 转换为绝对值的形式
y_grad = cv.convertScaleAbs(y_grad)  # 将图片转换为8位输出 	该函数对每个元素进行三步操作：缩放、绝对值、转换为无符号8位
# cv.imshow("x_grad", x_grad)
# cv.imshow("y_grad", y_grad)

dst = cv.add(x_grad, y_grad, dtype=cv.CV_16S)  # 将x轴方向的sobel算子的结果和y轴方向上的sobel算子的结果结合
dst = cv.convertScaleAbs(dst)
cv.imshow("gradient", dst)

result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = dst
cv.imshow("result", result)
cv.imshow('imgs', np.hstack((src, dst))) #合并对比显示
                                        # np.vstack():在竖直方向上堆叠
                                        # np.hstack():在水平方向上平铺
# cv.imwrite("./result.png", dst)

cv.waitKey(0)
cv.destroyAllWindows()
