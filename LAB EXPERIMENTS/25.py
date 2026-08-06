import cv2

img = cv2.imread(r"C:\Users\Sasha\Pictures\download.jpg",0)

grad = cv2.Scharr(img,cv2.CV_64F,1,0)

cv2.imshow("Original",img)
cv2.imshow("Gradient",grad)

cv2.waitKey(0)
cv2.destroyAllWindows()
