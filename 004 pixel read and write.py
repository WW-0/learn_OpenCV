import cv2

image0 = cv2.imread('01.jpg')
cv2.namedWindow('image0', cv2.WINDOW_FREERATIO)
cv2.imshow('image0', image0)
h, w, ch = image0.shape
for row in range(h):
    for col in range(w):
        b, g, r = image0[row, col]
        # b1=image0[row,col,0]
        # g1=image0[row,col,1]
        # r1=image0[row,col,2]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        image0[row, col] = [b, g, r]
cv2.namedWindow('image2', cv2.WINDOW_FREERATIO)
cv2.imshow('image2', image0)

cv2.waitKey(0)
cv2.destroyAllWindows()
