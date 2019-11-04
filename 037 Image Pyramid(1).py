# pyramid /ˈpɪrəmɪd/金字塔
import cv2


def pyramid_down(pyramid_images):
    level = len(pyramid_images)  # 理解1可以讲最外层括号看成列表，输出的就是最外层列表元素数目
                                 # 理解2输出的是矩阵行数
    print("level = ", level)
    for i in range(level - 1, -1, -1):  # 倒着输出
        expand = cv2.pyrUp(pyramid_images[i])  # 向上采样讲输入的数据再扩大回去，然后输出
        cv2.imshow("pyramid_down_" + str(i), expand)  # 经对比可发现，还原后的最大图片与输入原相等尺寸图片有信息丢失


def pyramid_up(image, level=3):
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv2.pyrDown(temp)
        pyramid_images.append(dst)
        # cv2.imshow("pyramid_up_" + str(i), dst) #如果此处输出，仅仅使用了下采样 底层图最大，每次减小一半放在上层
        temp = dst.copy()
    return pyramid_images


src = cv2.imread("01a.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)
# pyramid_up(src)
pyramid_down(pyramid_up(src))

cv2.waitKey(0)
cv2.destroyAllWindows()
