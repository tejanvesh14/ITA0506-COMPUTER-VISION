import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Sasha\Pictures\download.jpg")

pts1 = np.float32([[50,50],[300,50],[50,300],[300,300]])
pts2 = np.float32([[100,100],[350,100],[100,350],[350,350]])

H = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(img, H, (400,400))

cv2.imshow("Original", img)
cv2.imshow("DLT", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
