import cv2
import numpy as np

image0 = cv2.imread('08.jpg')
image1 = cv2.imread('01.jpg')
image0 = cv2.resize(image0, (image1.shape[1] , image1.shape[0])) #改变图片尺寸
cv2.imshow('image0', image0)
cv2.imshow('image1', image1)
h, w, ch = image0.shape
print('h, w, ch', h, w, ch)

add_result = np.zeros(image0.shape, image0.dtype)
cv2.add(image1, image0, add_result)                 #图像像素算数加法
cv2.imshow('add_result', add_result)

sub_result=np.zeros(image0.shape,image0.dtype)
cv2.subtract(image0,image1,sub_result)              #图像像素算数减法
cv2.imshow('sub_result',sub_result)

mul_result=np.zeros(image0.shape,image0.dtype)
cv2.multiply(image0,image1,mul_result)
cv2.imshow('mul_result',mul_result)

div_result=np.zeros(image0.shape,image0.dtype)
cv2.divide(image0,image1,div_result)
cv2.imshow('div_result',div_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
