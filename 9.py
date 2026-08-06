import cv2

video = cv2.VideoCapture("D:\Sasha\Downloads\WhatsApp Video 2026-06-18 at 2.00.31 PM.mp4")

fps = video.get(cv2.CAP_PROP_FPS)
delay = int(1000 / (fps * 1.5))  # 1.5x speed

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("1.5x Speed Video", frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
