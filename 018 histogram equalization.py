# equalization 均衡化
import cv2
import numpy as np
from matplotlib import pyplot as plt


def custom_hist(gray):
    h, w = gray.shape
    hist = np.zeros([256], dtype=np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1
    y_pos = np.arange(0, 256, 1, dtype=np.int32)
    plt.bar(y_pos, hist, align='center', color='r', alpha=0.5)
    plt.xticks(y_pos, y_pos)
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()


image0 = cv2.imread('01a.jpg', 0)
cv2.namedWindow('input', cv2.WINDOW_AUTOSIZE)
cv2.imshow('input', image0)
dst = cv2.equalizeHist(image0)
cv2.imshow('eh', dst)
dst1 = cv2.equalizeHist(dst)
custom_hist(image0)
custom_hist(dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
