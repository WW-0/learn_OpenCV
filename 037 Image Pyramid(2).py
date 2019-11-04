import cv2 as cv
import numpy as np

def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)  #先对图像进行高斯平滑，然后再进行降采样（将图像尺寸行和列方向缩减一半）
        pyramid_images.append(dst)
        cv.imshow("pyramid_demo_%s"%i,dst)
        temp = dst.copy()


src = cv.imread("01a.jpg")  #读取图片
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)    #创建GUI窗口,形式为自适应
cv.imshow("input image",src)    #通过名字将图像和窗口联系
pyramid_demo(src)
cv.waitKey(0)   #等待用户操作，里面等待参数是毫秒，我们填写0，代表是永远，等待用户操作
cv.destroyAllWindows()  #销毁所有窗口