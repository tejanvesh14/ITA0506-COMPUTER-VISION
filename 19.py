import cv2

img = cv2.imread(r"C:\Users\Sasha\Pictures\download.jpg", 0)

x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
y = cv2.Sobel(img, cv2.CV_64F, 0, 1)

xy = cv2.add(x, y)

cv2.imshow("Original", img)
cv2.imshow("Sobel XY", xy)

cv2.waitKey(0)
cv2.destroyAllWindows()
