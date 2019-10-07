# histogram /ˈhɪstəɡræm/ 直方图，柱状图
import cv2
import numpy as np
from matplotlib import pyplot as plt


def custom_hist(gray):
    h, w = gray.shape
    hist = np.zeros([256], dtype=np.uint32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1
    y_pos = np.arange(0, 256, 1, dtype=np.int32)
    plt.bar(y_pos, hist, align='center', color='r', alpha=1)  # 绘制直方图
    # 横坐标，柱子高度，柱子对齐方式，颜色，透明度
    plt.xticks(y_pos, y_pos)  # 设置横轴刻度
    plt.ylabel('Frequency')
    plt.title('histogram')
    plt.show()


def image_hist(image):
    cv2.imshow('input', image)
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):  # enumerate枚举，得到序列中索引位置以及对应值
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        # 原图，通道，掩膜，组数，像素范围
        plt.plot(hist, color=color)
        plt.xlim([1, 256])
    plt.show()


image0 = cv2.imread('01a.jpg')
cv2.namedWindow('input', cv2.WINDOW_AUTOSIZE)
gray = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)
cv2.imshow('input', gray)
# image_hist(image0)
custom_hist(gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
