import cv2
import numpy as np

image0 = cv2.imread('01a.jpg', 0)  # 读取图片转为灰度图
cv2.namedWindow('image0', cv2.WINDOW_FREERATIO)
cv2.imshow('image0', image0)

min, max, minloc, maxloc = cv2.minMaxLoc(image0)  # 得到一个单通道矩阵的最小值、最大值及其坐标
print('min: %.2f, max: %.2f' % (min, max))
print('min loc: ', minloc)
print('max loc: ', maxloc)

mean, stddev = cv2.meanStdDev(image0)  # 计算单通道矩阵均值和标准差
print('mean: %.2f,stddev: %.2f' % (mean, stddev))
image0[np.where(image0 < mean)] = 0  # 0为黑，255为白
image0[np.where(image0 > mean)] = 255  # np.where(条件)，若条件满足，返回索引值 ,np.where(条件，x,y)，满足返回x否则返回y
cv2.imshow('binary', image0)
# image0[np.where(image0<mean)]=255#反过来写并不能得到相反效果，此处为逻辑错误，小于平均值的都被改成255
# image0[np.where(image0>mean)]=0 #此时执行大于平均值时image0已经都变成大于平均值的数据，所以都符合该条件
image0 = cv2.bitwise_not(image0)
cv2.imshow('binary2', image0)

cv2.waitKey(0)
cv2.destroyAllWindows()
