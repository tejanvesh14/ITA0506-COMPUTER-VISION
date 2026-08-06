import cv2

image = cv2.imread(r"C:\Users\Sasha\Pictures\images.jpg")

blur_image = cv2.blur(image, (15, 15))

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blur_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
