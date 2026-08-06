import cv2

img = cv2.imread(r"C:\Users\Sasha\Pictures\download.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,th = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Object Detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
