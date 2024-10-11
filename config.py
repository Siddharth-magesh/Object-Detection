Model_Path = r'D:\Object-Detection\models\best.pt'   # Path to your trained model
Model_Name = 'yolov8s.pt'                            # Name of the YOLO model
Yaml_Path = 'data.yaml'                              # Path to the YAML file containing dataset details
Use_image = True                                     # Set to True to run on an image, False for video
Use_video = False                                    # Set to True to run on a video
Image_Path = r'D:\Object-Detection\example\4.jpg'    # Path to the input image
Video_Path = r'D:\Object-Detection\example\8.mp4'    # Path to the input video
Destination_Path = r'outputs'                        # Directory where output images/videos will be saved
class_names = [                                      # Class names of objects being detected
    "bus_stop",
    "do_not_enter",
    "do_not_stop",
    "do_not_turn_l",
    "do_not_turn_r",
    "do_not_u_turn",
    "enter_left_lane",
    "green_light",
    "left_right_lane",
    "no_parking",
    "parking",
    "ped_crossing",
    "ped_zebra_cross",
    "railway_crossing",
    "red_light",
    "stop",
    "t_intersection_l",
    "traffic_light",
    "u_turn",
    "warning",
    "yellow_light",
]