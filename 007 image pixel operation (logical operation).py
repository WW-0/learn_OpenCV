import cv2
import numpy as np

#creat image one
image0=np.zeros(shape=[400,400,3],dtype=np.uint8)
image0[100:200,100:200,1]=255
image0[100:200,100:200,2]=255
cv2.imshow('image0',image0)

#creat image two
image1=np.zeros(shape=[400,400,3],dtype=np.uint8)
image1[150:250,150:250,2]=255
cv2.imshow('image2',image1)

dst1=cv2.bitwise_and(image0,image1) #bitwise 逐位按位
dst2=cv2.bitwise_or(image1,image0) #对应像素对应通道 或运算
dst3=cv2.bitwise_xor(image0,image1)
image2=cv2.imread('01a.jpg')
dst4=cv2.bitwise_not(image2)

cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)

cv2.waitKey(0)
cv2.destroyAllWindows()

