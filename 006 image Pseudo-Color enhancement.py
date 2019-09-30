# 图像伪色彩增强
import cv2

image0 = cv2.imread('01.jpg')
print(type(image0))
print(image0)
cv2.namedWindow('image0', cv2.WINDOW_FREERATIO)
cv2.imshow('image0', image0)
image1 = cv2.applyColorMap(image0, cv2.COLORMAP_COOL)
cv2.namedWindow('image1', cv2.WINDOW_FREERATIO)
cv2.imshow('image1', image1)

color_image = cv2.applyColorMap(image0, cv2.COLORMAP_JET)
cv2.namedWindow('color_image', cv2.WINDOW_FREERATIO)
cv2.imshow('color_image', color_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
