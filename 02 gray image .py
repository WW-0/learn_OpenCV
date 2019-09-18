import cv2

"""Method1"""
image0 = cv2.imread('01.jpg', 0)
cv2.namedWindow('show gray', cv2.WINDOW_FREERATIO)
cv2.imshow('show gray', image0)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""Method2"""
image1 = cv2.imread('01.jpg')
cv2.namedWindow('input', cv2.WINDOW_FREERATIO)
cv2.imshow('input', image1)
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.png', gray)
cv2.namedWindow('gray', cv2.WINDOW_FREERATIO)
cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
