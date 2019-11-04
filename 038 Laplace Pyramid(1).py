import cv2


def laplaian_demo(pyramid_images):
    level = len(pyramid_images)
    for i in range(level - 1, -1, -1):
        if (i - 1) < 0:
            h, w = src.shape[:2]
            expand = cv2.pyrUp(pyramid_images[i], dstsize=(w, h))
            lpls = cv2.subtract(src, expand) + 127 #加127可能就是为了看起来方便
            cv2.imshow("lpls_" + str(i), lpls)
        else:
            h, w = pyramid_images[i - 1].shape[:2]  # （400，600，3） 只取400 600
            expand = cv2.pyrUp(pyramid_images[i], dstsize=(w, h))  # 扩大的图 i-1图像尺寸大于1
            lpls = cv2.subtract(pyramid_images[i - 1], expand) + 127  # 计算两个数组或数组和标量之间的每个元素差。也就是图像的相减操作
            cv2.imshow("lpls_" + str(i), lpls)                        #加127可能就是为了看起来方便


def pyramid_up(image, level=3):
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv2.pyrDown(temp)
        pyramid_images.append(dst)
        # cv.imshow("pyramid_up_" + str(i), dst)
        temp = dst.copy()
    return pyramid_images


src = cv2.imread("01a.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)
# pyramid_up(src)
laplaian_demo(pyramid_up(src))

cv2.waitKey(0)
cv2.destroyAllWindows()
