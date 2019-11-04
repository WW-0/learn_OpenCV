import cv2 as cv
import numpy as np

src = cv.imread("01a.jpg",0)
cv.imshow("input", src)

dst1 = cv.GaussianBlur(src, (5, 5), sigmaX=1.8 * 2.3)
dst2 = cv.GaussianBlur(src, (5, 5), sigmaX=2.5)
dst = dst1 - dst2
cv.imshow("gaussian sigmax1", dst1)
cv.imshow("gaussian sigmax2", dst2)
cv.imshow("DOG", dst)

cv.waitKey(0)
cv.destroyAllWindows()
