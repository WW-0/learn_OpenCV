# backprojection 反向投影
# 个人理解：通过感兴趣图像A的直方图，在源图像B中寻找和A有相同特征的部分
import cv2
import matplotlib.pyplot as plt


def back_projection_demo():
    sample = cv2.imread('01a target2.png')  # sample 样品，模板，被寻找的特征
    # hist2d_demo(sample)
    target = cv2.imread('01a.jpg')  # 源图片，要在原图片中寻找有相同特征的目标
    # hist2d_demo(target)
    roi_hsv = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV)
    target_hsv = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

    # show images
    cv2.imshow("sample", sample)
    cv2.imshow("target", target)

    roiHist = cv2.calcHist([roi_hsv], [0, 1], None, [32, 32], [0, 256, 0, 256])  # 直方图
    cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)  # 归一化
    dst = cv2.calcBackProject([target_hsv], [0, 1], roiHist, [0, 256, 0, 256], 1)  # 反向投影
    # 源图片(HSV)，通道列表，模板直方图，直方图bin范围，比例因子一般为1
    cv2.imshow("backProjectionDemo", dst)


def hist2d_demo(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
    dst = cv2.resize(hist, (400, 400))
    cv2.imshow("image", image)
    cv2.imshow("hist", dst)
    plt.imshow(hist, interpolation='nearest')
    plt.title("2D Histogram")
    plt.show()


back_projection_demo()

cv2.waitKey(0)
cv2.destroyAllWindows()
