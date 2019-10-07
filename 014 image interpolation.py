import cv2

image0 = cv2.imread('01a.jpg')
cv2.namedWindow('image0', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image0', image0)

h, w = image0.shape[:2]
print(h, w)
dst = cv2.resize(image0, (w * 2, h * 2), fx=1.75, fy=1.75, interpolation=cv2.INTER_NEAREST)
cv2.imshow('INTER_NEAREST', dst)

dst = cv2.resize(image0, (w * 2, h * 2), interpolation=cv2.INTER_LINEAR)
cv2.imshow("INTER_LINEAR", dst)

dst = cv2.resize(image0, (w * 2, h * 2), interpolation=cv2.INTER_CUBIC)
cv2.imshow("INTER_CUBIC", dst)

dst = cv2.resize(image0, (w * 2, h * 2), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("INTER_LANCZOS4", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
