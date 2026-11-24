import cv2
from ultralytics import YOLO

model = YOLO("best (1).pt")  

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access your local camera.")
    exit()

print("Camera is now live!")
print(" To close the video, click on the video window and press 'q' on your keyboard.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab video frame.")
        break

    results = model(frame, conf=0.25, verbose=False)

    annotated_frame = results[0].plot()

    cv2.imshow("VS Code Live Model Inference", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Camera closed successfully.")
