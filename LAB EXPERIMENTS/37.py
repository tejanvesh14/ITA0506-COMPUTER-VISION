import cv2

cap = cv2.VideoCapture(r"D:\Sasha\Downloads\WhatsApp Video 2026-06-18 at 2.00.31 PM.mp4")

frames=[]

while True:
    ret,frame=cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

for frame in frames[::-1]:
    cv2.imshow("Reverse Video",frame)
    if cv2.waitKey(30)==27:
        break

cv2.destroyAllWindows()
