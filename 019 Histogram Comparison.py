import cv2

image1 = cv2.imread('01a.jpg')
image2 = cv2.imread('04.jpg')
image3 = cv2.imread('01a.jpg')
image4 = cv2.imread('01a.jpg')

cv2.imshow('input1', image1)
cv2.imshow('inout2', image2)
cv2.imshow('input3', image3)
cv2.imshow('input4', image4)

hsv1 = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
hsv3 = cv2.cvtColor(image3, cv2.COLOR_BGR2HSV)
hsv4 = cv2.cvtColor(image4, cv2.COLOR_BGR2HSV)

hist1 = cv2.calcHist([hsv1], [0, 1], None, [60, 64], [0, 180, 0, 256])  # 统计直方图
hist2 = cv2.calcHist([hsv2], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist3 = cv2.calcHist([hsv3], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist4 = cv2.calcHist([hsv4], [0, 1], None, [60, 64], [0, 180, 0, 256])

cv2.normalize(hist1, hist1, 0, 1.0, cv2.NORM_MINMAX)  # 归一化
cv2.normalize(hist2, hist2, 0, 1.0, cv2.NORM_MINMAX)
cv2.normalize(hist3, hist3, 0, 1.0, cv2.NORM_MINMAX)
cv2.normalize(hist4, hist4, 0, 1.0, cv2.NORM_MINMAX)

methods = [cv2.HISTCMP_CORREL, cv2.HISTCMP_CHISQR,
           cv2.HISTCMP_INTERSECT, cv2.HISTCMP_BHATTACHARYYA]  # 比较标准
str_method = ""
for method in methods:
    src1_src2 = cv2.compareHist(hist1, hist2, method)
    src3_src4 = cv2.compareHist(hist3, hist4, method)
    if method == cv2.HISTCMP_CORREL:
        str_method = "Correlation"
    if method == cv2.HISTCMP_CHISQR:
        str_method = "Chi-square"
    if method == cv2.HISTCMP_INTERSECT:
        str_method = "Intersection"
    if method == cv2.HISTCMP_BHATTACHARYYA:
        str_method = "Bhattacharyya"

    print("%s src1_src2 = %.2f, src3_src4 = %.2f" % (str_method, src1_src2, src3_src4))

cv2.waitKey(0)
cv2.destroyAllWindows()
