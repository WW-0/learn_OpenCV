import cv2
import numpy as np
from scipy import signal

image = cv2.imread('01a.jpg', cv2.IMREAD_GRAYSCALE)
h, w = image.shape[:2]  # 图片的高度和宽度
print('imagesize={}-{}'.format(w, h))
cv2.imshow("Image", image)

# roberts算子
# roberts_cross_v = np.array( [[ 0, 0, 0 ],
#                              [ 0, 1, 0 ],
#                              [ 0, 0,-1 ]] )
#
# roberts_cross_h = np.array( [[ 0, 0, 0 ],
#                              [ 0, 0, 1 ],
#                              [ 0,-1, 0 ]] )
roberts_cross_v = np.array([[1, 0],
                            [0, -1]])

roberts_cross_h = np.array([[0, 1],
                            [-1, 0]])
# 垂直
vertical = signal.convolve2d(image, roberts_cross_v, boundary='symm')  # 卷积计算
# in1；in2；mode决定返回卷积结果的大小默认是full；boundary填充模式默认fill，symm镜像模式；fillvalue填充值(fill模式下有效)
vertical1 = vertical.astype(np.uint8)  # 转换数据类型
cv2.imshow("vertical", vertical1)

# 水平
horizontal = signal.convolve2d(image, roberts_cross_h, boundary='symm')
horizontal1 = horizontal.astype(np.uint8)
cv2.imshow("horizontal", horizontal1)

output_image = np.sqrt(np.square(horizontal) + np.square(vertical))
output_image = output_image.astype(np.uint8)
cv2.imshow("output_image", output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
