import cv2

image = cv2.imread(r"C:\Users\Sasha\Pictures\images.jpg")

big_image = cv2.resize(image, (800, 600))

cv2.imshow("Original Image", image)
cv2.imshow("Big Image", big_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
