import cv2

image0 = cv2.imread('01a.jpg')
cv2.namedWindow('RGB', cv2.WINDOW_AUTOSIZE)
cv2.imshow('RGB', image0)

# RGB to HSV
hsv0 = cv2.cvtColor(image0, cv2.COLOR_BGR2HSV)  # H:0-180 S:0-255 V:0-255
cv2.imshow('HSV0', hsv0)

# RGB to YUV
yuv = cv2.cvtColor(image0, cv2.COLOR_BGR2YUV)
cv2.imshow('YUV', yuv)

# RGB to YCrCb
ycrcb = cv2.cvtColor(image0, cv2.COLOR_BGR2YCrCb)
cv2.imshow("ycrcb", ycrcb)

image1 = cv2.imread('01a.jpg')
cv2.imshow("image1", image1)
hsv1 = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv1, (35, 43, 46), (99, 255, 255))
# lower(35,43,46)===>0,upper(99,255,255)200==>0,others==>255
cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
