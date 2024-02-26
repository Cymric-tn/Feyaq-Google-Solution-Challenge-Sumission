
import cv2
import cvzone
from ultralytics import YOLO
import math
import threading
from message import send_message

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

model = YOLO("yolo-weights/yolov8l.pt")

isAgitated = False
messageSent = False

while True:
    success, img = cap.read()
    results = model(img, stream=True, conf=0.4)

    for result in results:
        names = result.names
        boxes = result.boxes
        for box in boxes:
            conf = math.ceil(box.conf[0]*100)/100
            cls = names[int(box.cls[0])]

            if cls == "person":
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                status = "Agitation" if isAgitated else "Normal"
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 200) if isAgitated else(0, 200, 0), 3)
                cvzone.putTextRect(img, f"{status}: {conf} - {cls}", (max(0, x1), max(50, y1 - 20)), colorR=(0, 0, 200) if isAgitated else(0, 200, 0))

    cv2.imshow("Image", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord(' '):
        isAgitated = not(isAgitated)

        if isAgitated == False:
            messageSent = False

    elif key == ord('q'):
        break

    if isAgitated == True and messageSent == False:
        threading.Thread(target=send_message).start()
        messageSent = True

cap.release()
cv2.destroyAllWindows()
