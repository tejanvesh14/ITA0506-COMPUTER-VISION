import cv2

cap = cv2.VideoCapture(r"D:\Sasha\Downloads\WhatsApp Video 2026-06-18 at 2.00.31 PM.mp4")

bg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret,frame = cap.read()
    if not ret:
        break

    mask = bg.apply(frame)

    cv2.imshow("Vehicle Detection",mask)

    if cv2.waitKey(30)==27:
        break

cap.release()
cv2.destroyAllWindows()
