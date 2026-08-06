import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Sasha\Pictures\images.jpg")

image = cv2.resize(image, (200, 200))

x, y = 100, 100
dx, dy = 10, 10

while True:
    canvas = np.zeros((600, 800, 3), dtype=np.uint8)

    h, w = image.shape[:2]

    canvas[y:y+h, x:x+w] = image

    cv2.imshow("Moving Image", canvas)

    x += dx
    y += dy

    if x + w >= 800 or x <= 0:
        dx = -dx
    if y + h >= 600 or y <= 0:
        dy = -dy

    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()
