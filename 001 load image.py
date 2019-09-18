import cv2

"""读取图片并显示"""
image1 = cv2.imread("01.jpg")
cv2.namedWindow('image1', cv2.WINDOW_NORMAL)
cv2.imshow('image1', image1)
cv2.waitKey(0)  # delay<=0将无期限等待，如果>0就延时delay毫秒
cv2.destroyAllWindows()

"""转换图片格式"""
image2 = cv2.imread('02.png')
cv2.imwrite('03.jpg', image2)
image3 = cv2.imread('03.jpg')
cv2.namedWindow('image3', cv2.WINDOW_NORMAL)
cv2.imshow('image3', image3)
cv2.waitKey(0)
cv2.destroyAllWindows()
