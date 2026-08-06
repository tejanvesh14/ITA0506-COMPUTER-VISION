import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Sasha\Pictures\download.jpg")

kernel = np.array([[1,1,1],
                   [1,-8,1],
                   [1,1,1]])

sharp = cv2.filter2D(img,-1,kernel)

cv2.imshow("Original",img)
cv2.imshow("Sharpen",sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
