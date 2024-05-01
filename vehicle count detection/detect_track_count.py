import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import*

# Initialize YOLO model
model = YOLO('yolov8s.pt')

# Define class list
class_list = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

# Initialize tracker
tracker = Tracker()

# Open video capture
cap = cv2.VideoCapture('small.mp4')

# Initialize variables
down = {}
up = {}
counter_down = []
counter_up = []
paused = False

# Function to toggle pause/play state
def toggle_pause():
    global paused
    paused = not paused

while True:
    # If not paused, read a frame from the video
    if not paused:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame
        frame = cv2.resize(frame, (1020, 500))

        # Predict using YOLO model
        results = model.predict(frame)
        a = results[0].boxes.data.detach().cpu().numpy()

        # Convert predictions to DataFrame
        px = pd.DataFrame(a).astype("float")

        # Extract cars from predictions
        list = []
        for index, row in px.iterrows():
            x1 = int(row[0])
            y1 = int(row[1])
            x2 = int(row[2])
            y2 = int(row[3])
            d = int(row[5])
            c = class_list[d]
            if 'car' in c:
                list.append([x1, y1, x2, y2])

        # Update tracker
        bbox_id = tracker.update(list)

        # Process tracked objects
        for bbox in bbox_id:
            x3, y3, x4, y4, id = bbox
            cx = int(x3 + x4) // 2
            cy = int(y3 + y4) // 2

            # Define line positions
            red_line_y = 198
            blue_line_y = 268
            offset = 7

            # Count cars crossing lines
            if red_line_y < (cy + offset) and red_line_y > (cy - offset):
                down[id] = cy
            if id in down:
                if blue_line_y < (cy + offset) and blue_line_y > (cy - offset):
                    counter_down.append(id)
            if blue_line_y < (cy + offset) and blue_line_y > (cy - offset):
                up[id] = cy
            if id in up:
                if red_line_y < (cy + offset) and red_line_y > (cy - offset):
                    counter_up.append(id)

            # Draw lines and text on frame
            cv2.line(frame, (172, 198), (774, 198), (0, 0, 255), 3)
            cv2.putText(frame, 'red line', (172, 198), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.line(frame, (8, 268), (927, 268), (255, 0, 0), 3)
            cv2.putText(frame, 'blue line', (8, 268), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'going down - ' + str(len(counter_down)), (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.putText(frame, 'going up - ' + str(len(counter_up)), (60, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.imshow("frames", frame)

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # If the 'p' key is pressed, toggle pause/play
    if key == ord('p'):
        toggle_pause()

    # If the 'Esc' key is pressed, exit
    if key == 27:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
