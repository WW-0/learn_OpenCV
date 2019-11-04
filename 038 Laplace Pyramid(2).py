import cv2 as cv


def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)  # 先对图像进行高斯平滑，然后再进行降采样（将图像尺寸行和列方向缩减一半）
        pyramid_images.append(dst)
        cv.imshow("pyramid_demo_%s" % i, dst)
        temp = dst.copy()
    return pyramid_images


def lapalian_demo(image):
    pyramid_images = pyramid_demo(image)  # 拉普拉斯需要用到高斯金字塔结果
    level = len(pyramid_images)
    for i in range(level - 1, -1, -1):  # 从后向前2,1,0
        if (i - 1) < 0:
            h, w = image.shape[:2]
            expand = cv.pyrUp(pyramid_images[i], dstsize=(w, h))  # 先上采样
            lapls = cv.subtract(image, expand)  # 使用高斯金字塔上一个减去当前上采样获取的结果，才是拉普拉斯金字塔
        else:
            h, w = pyramid_images[i - 1].shape[:2]
            expand = cv.pyrUp(pyramid_images[i], dstsize=(w, h))
            lapls = cv.subtract(pyramid_images[i - 1], expand)
        cv.imshow("lapls_down_%s" % i, lapls)


src = cv.imread("01a.jpg")  # 读取图片
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)  # 创建GUI窗口,形式为自适应
cv.imshow("input image", src)  # 通过名字将图像和窗口联系
lapalian_demo(src)
cv.waitKey(0)  # 等待用户操作，里面等待参数是毫秒，我们填写0，代表是永远，等待用户操作
cv.destroyAllWindows()  # 销毁所有窗口
