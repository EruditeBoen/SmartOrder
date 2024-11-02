import cv2
import numpy as np
import onnx, ast
from yolov7 import YOLOv7
import pyfirmata
import random
import time

comport = '/dev/ttyACM0'

board = pyfirmata.Arduino(comport)

right = board.get_pin('d:9:o')
right.write(0)
wrong = board.get_pin('d:10:o')
wrong.write(0)

# Initialize the webcam
cap = cv2.VideoCapture(0)

width = 1920
height = 1080

# Initialize YOLOv7 object detector
model_path = "models/yolov7_384x640.onnx"
yolov7_detector = YOLOv7(model_path, conf_thres=0.5, iou_thres=0.5)

m = onnx.load('models/yolov7_384x640.onnx')
props = { p.key : p.value for p in m.metadata_props }
if 'names' in props:
    names = ast.literal_eval(props['names'])

cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)

ingredients = names

order_input = [ingredient for ingredient in input("What would you like on your death burger? (State ingredients seperated by a space): ").split(" ")]
# order_input = ["mouse", "spoon"]

on_burger = [""]

what_i_want = "I want "
for ingredient in order_input:
    what_i_want += ingredient + ", "
what_i_want = what_i_want[:-2]
print("Customer: " + what_i_want)

print("Cashier: Ok I'll be right out with you order")

cv2.namedWindow("Validation", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Validation", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

color = (255, 255, 255)

making = True
while making:
    color_screen = np.zeros((height, width, 3), np.uint8)
    color_screen[:] = (255, 255, 255)
    cv2.imshow("Validation", color_screen)


    # Read frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Update object localizer
    boxes, scores, class_ids = yolov7_detector(frame)
    next_ingredient = ""
    if len(class_ids) == 1:
        next_ingredient = names[class_ids[0]]
    elif len(class_ids) == 0:
        print("Put something on the screen")
        

    combined_img = yolov7_detector.draw_detections(frame)
    cv2.imshow("Detected Objects", combined_img)

    # next_ingredient = input('Next ingredient (enter "Done" if there is no more ingredients): ')

    if next_ingredient not in on_burger:

        if next_ingredient in order_input and next_ingredient not in on_burger:
            right.write(1)
            color = (0, 255, 0)
            print(f"{next_ingredient} is the correct ingredient!")
            on_burger.append(next_ingredient)
            time.sleep(1)
            right.write(0)
        elif next_ingredient not in order_input:
            wrong.write(1)
            print(f"{next_ingredient} is not on the receipt! Take it off!!")
            color = (0, 0, 255)
            time.sleep(1)
            wrong.write(0)

    else:
        print("put something else on burger")
        color = (255, 255, 255)
    
    if (set(on_burger) == set(order_input)):
        print("Waiter: Here is your order! Have a good one!")
        print("Customer: Thanks!!")
        making = False
    
    color_screen[:] = color
    cv2.imshow("Validation", color_screen)
    time.sleep(1)
    

    cv2.waitKey(0)
