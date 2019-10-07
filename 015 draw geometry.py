import cv2
import numpy as np

image = np.zeros((512, 512, 3), dtype=np.uint8)

cv2.rectangle(image, (100, 100), (300, 300), (255, 0, 0), 2, cv2.LINE_8, 0)  # 矩形
# 输出图像，第一个坐标点，第二个坐标点，线颜色，线粗细(默认1)，线类型(4连接、8连接、抗锯齿)，坐标点小数点位数
cv2.circle(image, (300, 300), 100, (0, 0, 255), 2, cv2.LINE_8, 0)  # 圆
# 输出图像，圆心，半径，颜色，粗细，线类型，小数点位数
cv2.ellipse(image, (300, 300), (200, 100), 360, 0, 360, (0, 255, 0), 2, cv2.LINE_AA, 0)  # 椭圆
# 输出图像，中心点位置，椭圆尺寸(长短轴)，椭圆的旋转角度(顺)，绘制起始角度，绘制终止角度，颜色，粗细，类型，小数点位数
cv2.imshow("image", image)
cv2.waitKey(0)

for i in range(100000):
    image[:, :, :] = 0
    x1 = np.random.rand() * 512
    y1 = np.random.rand() * 512
    x2 = np.random.rand() * 512
    y2 = np.random.rand() * 512

    b = np.random.randint(0, 256)
    g = np.random.randint(0, 256)
    r = np.random.randint(0, 256)
    # cv.line(image, (np.int(x1), np.int(y1)), (np.int(x2), np.int(y2)), (b, g, r), 4, cv.LINE_8, 0)
    cv2.rectangle(image, (np.int(x1), np.int(y1)), (np.int(x2), np.int(y2)), (b, g, r), 1, cv2.LINE_8, 0)
    cv2.imshow("image", image)
    c = cv2.waitKey(20)
    if c == 27:  # ESC的键值
        break  # 如果检测到ECS按键，结束循环

cv2.destroyAllWindows()
