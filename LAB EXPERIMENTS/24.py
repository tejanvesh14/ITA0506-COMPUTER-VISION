import cv2

img = cv2.imread(r"C:\Users\Sasha\Pictures\download.jpg")

blur = cv2.GaussianBlur(img,(5,5),0)
high = cv2.addWeighted(img,2.5,blur,-1.5,0)

cv2.imshow("Original",img)
cv2.imshow("High Boost",high)

cv2.waitKey(0)
cv2.destroyAllWindows()
