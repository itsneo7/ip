from pathlib import Path
import cv2
from ultralytics import YOLO

input_dir = Path("test_images")
output_dir = Path("results")

output_dir.mkdir(parents=True, exist_ok=True)

model = YOLO("best (1).pt")

image_extensions = ("*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG")
image_paths = []
for ext in image_extensions:
    image_paths.extend(input_dir.glob(ext))

if not image_paths:
    print(f"No images found in '{input_dir}'. Please add some images and try again.")
    exit()

print(f"Found {len(image_paths)} images. Starting human detection...")

for img_path in image_paths:
    frame = cv2.imread(str(img_path))
    if frame is None:
        print(f"Skipping corrupt or unreadable image: {img_path.name}")
        continue

    results = model(frame, classes=[0], verbose=False)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = float(box.conf[0]) # Also fixed confidence tensor structure
            
            # Draw green bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Overlay confidence score
            label = f"Person: {confidence:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 6. Save the processed image to the results folder
    output_path = output_dir / img_path.name
    cv2.imwrite(str(output_path), frame)
    print(f"Processed and saved: {output_path}")

print(f"\n Success! All processed images are saved in the '{output_dir}' folder.")
