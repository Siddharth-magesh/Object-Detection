import cv2
from pathlib import Path
import config  
import os
from ultralytics import YOLO
import time 

model = YOLO(config.Model_Path)

#Function To Detect Image
def detect_image(image_path, destination_path):
    image_path = image_path.strip('"').replace("\\", "/")
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    results = model(img)

    boxes = results[0].boxes.xyxy
    confidences = results[0].boxes.conf
    labels = results[0].boxes.cls

    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    result_image_filename = f'result_image_{timestamp}.jpg'
    result_image_path = Path(destination_path) / result_image_filename


    for box, confidence, label in zip(boxes, confidences, labels):
        x1, y1, x2, y2 = map(int, box) 
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2) 
        
        label_name = config.class_names[int(label)]
        label_text = f'{label_name} {confidence:.2f}'
        cv2.putText(img, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


    print(f"Saving result image to: {result_image_path}")
    cv2.imwrite(str(result_image_path), img)
    print(f'Results saved as {result_image_path}')


# Function to detect objects in a video
def detect_video(video_path, destination_path):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found at {video_path}")
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Error opening video stream or file: {video_path}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    result_video_path = Path(destination_path) / 'result_video.mp4'
    out = cv2.VideoWriter(str(result_video_path), cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    print(f"Processing video: {video_path}")
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        annotated_frame = results[0].plot()
        out.write(annotated_frame)
    cap.release()
    out.release()

    print(f'Results saved as {result_video_path}')

if __name__ == "__main__":
    if config.Use_image and config.Image_Path:
        detect_image(config.Image_Path, config.Destination_Path)
    elif config.Use_video and config.Video_Path:
        detect_video(config.Video_Path, config.Destination_Path)
    else:
        print("No valid input source. Please set either an image or video path in the config.")
