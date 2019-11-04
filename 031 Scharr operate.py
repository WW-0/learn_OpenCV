import cv2 as cv
#Scharr算子(Sobel算子的增强版，效果更突出)
def Scharr_demo(image):
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)   #对x求一阶导
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)   #对y求一阶导
    gradx = cv.convertScaleAbs(grad_x)  #用convertScaleAbs()函数将其转回原来的uint8形式 该函数对每个元素进行三步操作：缩放、绝对值、转换为无符号8位
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient_x", gradx)  #x方向上的梯度
    cv.imshow("gradient_y", grady)  #y方向上的梯度
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradient", gradxy)
src = cv.imread('01a.jpg')
cv.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
cv.imshow('input_image', src)
Scharr_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()