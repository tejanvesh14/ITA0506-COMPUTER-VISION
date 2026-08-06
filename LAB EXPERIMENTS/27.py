import cv2

img = cv2.imread(r"C:\Users\Sasha\Pictures\download.jpg")

crop = img[50:250,50:250]

cv2.imshow("Original", img)
cv2.imshow("Crop", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()
