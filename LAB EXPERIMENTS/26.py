import cv2

img = cv2.imread(r"C:\Users\Sasha\Pictures\download.jpg")
logo = cv2.imread(r"C:\Users\Sasha\Pictures\logo.jpg")

logo = cv2.resize(logo, (100,100))

img[0:100,0:100] = cv2.addWeighted(img[0:100,0:100], 1, logo, 0.5, 0)

cv2.imshow("Watermark", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
