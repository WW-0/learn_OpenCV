import cv2

image0=cv2.imread('01a.jpg')
cv2.namedWindow('rgb',cv2.WINDOW_AUTOSIZE)
cv2.imshow('RGB',image0)

#RGB to HSV
hsv=cv2.cvtColor(image0,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',hsv)


cv2.waitKey(0)
cv2.destroyAllWindows()


# # RGB to HSV
# hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
# cv.imshow("hsv", hsv)
#
# # RGB to YUV
# yuv = cv.cvtColor(src, cv.COLOR_BGR2YUV)
# cv.imshow("yuv", yuv)
#
# # RGB to YUV
# ycrcb = cv.cvtColor(src, cv.COLOR_BGR2YCrCb)
# cv.imshow("ycrcb", ycrcb)
#
# src2 = cv.imread("test.png");
# cv.imshow("src2", src2)
# hsv = cv.cvtColor(src2, cv.COLOR_BGR2HSV)
# mask = cv.inRange(hsv, (35, 43, 46), (99, 255, 255))
# cv.imshow("mask", mask)
#
# cv.waitKey(0)
# cv.destroyAllWindows()
