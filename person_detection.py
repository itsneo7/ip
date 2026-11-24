import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt") 

cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("Error: Could not open the live camera feed.")
    exit()

print("Live camera feed started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    results = model(frame, classes=[0], verbose=False)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = float(box.conf[0])
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            label = f"Person: {confidence:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Live Human Detection Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
