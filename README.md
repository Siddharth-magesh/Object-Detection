### Road Sign Detection Project: README

This project demonstrates an object detection system using a custom-trained YOLOv8 model to detect objects in images and videos. The project includes two modules: one for training a YOLO model (`train_model.py`) and another for object detection in images and videos (`detect_object.py`). The system can detect various road signs, such as stop signs, traffic lights, pedestrian crossings, and more.

---

## Table of Contents

1. [Installation](#installation)
2. [Setup and Configuration](#setup-and-configuration)
3. [Running the Project](#running-the-project)
4. [Project Structure](#project-structure)
5. [Editing `config.py`](#editing-configpy)
6. [How the Modules Work](#how-the-modules-work)
7. [Troubleshooting](#troubleshooting)

---

## Installation

### Step 1: Install Anaconda

Make sure Anaconda is installed. You can download and install it from the official website:  
[https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)

### Step 2: Create an Anaconda Environment

To manage dependencies and avoid conflicts, create a new environment:

```bash
conda create -n road_sign_detection python=3.8
conda activate road_sign_detection
```

### Step 3: Install Dependencies

Run the following commands to install the required packages for YOLOv8, OpenCV, and other dependencies:

```bash
pip install ultralytics
pip install opencv-python
pip install pathlib
```

Alternatively, you can install the required packages by using the `requirements.txt` file if provided:

```bash
pip install -r requirements.txt
```

---

## Setup and Configuration

### Step 1: Clone or Download the Repository

Clone this repository to your local machine or download the project files.

```bash
git clone https://github.com/your-repo/road_sign_detection.git
cd road_sign_detection
```

### Step 2: Set up `config.py`

The `config.py` file is essential for configuring model paths, input files, and output directories. Below is a description of the configuration parameters.

```python
Model_Path = r'D:\Object-Detection\models\best.pt'   # Path to your trained model
Model_Name = 'yolov8s.pt'                            # Name of the YOLO model
Yaml_Path = 'data.yaml'                              # Path to the YAML file containing dataset details
Use_image = True                                     # Set to True to run on an image, False for video
Use_video = False                                    # Set to True to run on a video
Image_Path = r'D:\Object-Detection\example\4.jpg'    # Path to the input image
Video_Path = r'D:\Object-Detection\example\8.mp4'    # Path to the input video
Destination_Path = r'outputs'                        # Directory where output images/videos will be saved
class_names = [                                      # Class names of objects being detected
    "bus_stop", "do_not_enter", "do_not_stop", "do_not_turn_l", "do_not_turn_r",
    "do_not_u_turn", "enter_left_lane", "green_light", "left_right_lane",
    "no_parking", "parking", "ped_crossing", "ped_zebra_cross", "railway_crossing",
    "red_light", "stop", "t_intersection_l", "traffic_light", "u_turn", "warning",
    "yellow_light",
]
```

---

## Running the Project

### Step 1: Train the YOLOv8 Model

If you need to train the YOLOv8 model, run the `train_model.py` file. This will download the model, train it on your dataset, and evaluate it.

```bash
python train_model.py
```

Training will use the dataset path specified in the `Yaml_Path` field of the `config.py` file.

### Step 2: Detect Objects in an Image or Video

To detect objects in an image or video, run the `detect_object.py` file. Depending on your settings in `config.py`, the script will detect objects either in the image or video, draw bounding boxes, and save the result.

```bash
python detect_object.py
```

- If `Use_image = True`, it will process the image in `Image_Path` and save the output.
- If `Use_video = True`, it will process the video in `Video_Path` and save the output.

### Output

The processed images or videos, with bounding boxes and labels, will be saved in the directory specified by `Destination_Path`.

---

## Project Structure

```
.
├── config.py            # Configuration file for setting paths and model options
├── train_model.py       # Script to train and evaluate the YOLOv8 model
├── detect_object.py     # Script to detect objects in images and videos
├── requirements.txt     # List of required dependencies (optional)
├── README.md            # Detailed project documentation
├── models/              # Directory for storing trained YOLO models
├── datasets/            # Directory for your dataset
│   ├── train/           # Training data
│   ├── valid/           # Validation data
│   └── test/            # Test data
└── outputs/             # Output directory for results
```

---

## Editing `config.py`

The `config.py` file controls how the scripts interact with the input data, output files, and the YOLO model. Here’s a breakdown of how you can modify it:

1. **Model Path**:

   - `Model_Path`: Path to your pre-trained or custom YOLO model (`.pt` file).
   - `Model_Name`: The YOLOv8 model name or any other name you prefer.

2. **Input Files**:

   - `Use_image`: Set to `True` to detect objects in an image.
   - `Use_video`: Set to `True` to detect objects in a video.
   - `Image_Path`: Path to the input image (used when `Use_image = True`).
   - `Video_Path`: Path to the input video (used when `Use_video = True`).

3. **Output**:

   - `Destination_Path`: The directory where output files (annotated images/videos) will be saved.

4. **Class Names**:
   - `class_names`: Modify this list if you're using a different set of objects for detection. This project is designed for road signs but can be extended.

---

## How the Modules Work

### `train_model.py`

This script loads the YOLOv8 model specified in `config.py`, trains it on the dataset, and evaluates its performance.

Key Steps:

- Download the YOLO model.
- Train the model on your dataset using the `data.yaml` file.
- Evaluate the trained model and output metrics.

### `detect_object.py`

This script handles object detection for both images and videos:

- **Image**: Detects objects in the image specified by `Image_Path`, draws bounding boxes, and saves the output.
- **Video**: Detects objects in each frame of the video specified by `Video_Path`, annotates each frame, and saves the output video.

---

## Troubleshooting

1. **Model Not Found**: Ensure the model path is correct in `config.py`. If the model hasn’t been trained yet, use the `train_model.py` script to train a model.
2. **Invalid Image Path**: If you encounter an error saying the image/video file was not found, double-check the paths in `config.py` to ensure they are correct and accessible.

3. **Output Directory Not Found**: If no results are being saved, make sure the output directory exists, or let the script create it automatically.

---

This concludes the setup and usage instructions. Happy coding!
