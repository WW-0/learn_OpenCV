import cv2 as cv
import numpy as np

src = cv.imread("01a.jpg", 0)
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

robert_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
robert_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)

prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)

robert_grad_x = cv.filter2D(src, cv.CV_32F, robert_x)  # 卷积操作
robert_grad_y = cv.filter2D(src, cv.CV_32F, robert_y)
robert_grad_x = cv.convertScaleAbs(robert_grad_x)  # 该函数对每个元素进行三步操作：缩放、绝对值、转换为无符号8位
robert_grad_y = cv.convertScaleAbs(robert_grad_y)

prewitt_grad_x = cv.filter2D(src, cv.CV_32F, prewitt_x)
prewitt_grad_y = cv.filter2D(src, cv.CV_32F, prewitt_y)
prewitt_grad_x = cv.convertScaleAbs(prewitt_grad_x)
prewitt_grad_y = cv.convertScaleAbs(prewitt_grad_y)

cv.imshow("robert x", robert_grad_x);
cv.imshow("robert y", robert_grad_y);
cv.imshow("prewitt x", prewitt_grad_x);
cv.imshow("prewitt y", prewitt_grad_y);

# h, w = src.shape[:2]
# robert_result = np.zeros([h, w * 2, 3], dtype=src.dtype)
# robert_result[0:h, 0:w, :] = robert_grad_x
# robert_result[0:h, w:2 * w, :] = robert_grad_y
# cv.imshow("robert_result", robert_result)

output_robert = np.sqrt(np.square(robert_grad_x) + np.square(robert_grad_y))
output_robert = output_robert.astype(np.uint8)
cv.imshow("robert_image", output_robert)

# prewitt_result = np.zeros([h, w * 2, 3], dtype=src.dtype)
# prewitt_result[0:h, 0:w, :] = prewitt_grad_x
# prewitt_result[0:h, w:2 * w, :] = prewitt_grad_y
# cv.imshow("prewitt_result", prewitt_result)

output_prewitt = np.sqrt(np.square(prewitt_grad_x) + np.square(prewitt_grad_y))
output_prewitt = output_prewitt.astype(np.uint8)
cv.imshow("prewitt_image", output_prewitt)

cv.waitKey(0)
cv.destroyAllWindows()
