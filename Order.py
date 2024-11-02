import cv2
import numpy as np
import onnx, ast
from yolov7 import YOLOv7
import random
import time

# Initialize the webcam
cap = cv2.VideoCapture(0)

width = 3840
height = 2160

# Initialize YOLOv7 object detector
model_path = "models/yolov7_training.onnx"
yolov7_detector = YOLOv7(model_path, conf_thres=0.5, iou_thres=0.5)

m = onnx.load('models/yolov7_training.onnx')
props = { p.key : p.value for p in m.metadata_props }
if 'names' in props:
    names = ast.literal_eval(props['names'])

print("Here are the classes within the model")
print(names)

cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)

ingredients = names

order_input = [ingredient for ingredient in input("What would you like on your burger? (List something from the list above and state ingredients seperated by a space): ").split(" ")]
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
    if len(class_ids) == 0:
        print("Put something on the burger!")

    objects_detected = [names[class_id] for class_id in class_ids]
        

    combined_img = yolov7_detector.draw_detections(frame)
    cv2.imshow("Detected Objects", combined_img)

    # next_ingredient = input('Next ingredient (enter "Done" if there is no more ingredients): ')

    if (set(on_burger[1:]) == set(order_input)):
        print("Waiter: Here is your order! Have a good one!")
        print("Customer: Thanks!!")
        making = False

    right = all(next_ingredient in order_input for next_ingredient in objects_detected)
    not_on_burger = any(next_ingredient not in on_burger for next_ingredient in objects_detected)

    if not_on_burger:

        if right and not_on_burger:
            color = (0, 255, 0)
            print(f"All is good")
            for next_ingredient in objects_detected:
                if next_ingredient not in on_burger:
                    on_burger.append(next_ingredient)
        elif not right:
            print(f"Something is not right! Take it off!!")
            color = (0, 0, 255)

    else:
        print("Put something else on burger")
        color = (255, 255, 255)


    color_screen[:] = color
    cv2.imshow("Validation", color_screen)

    print(on_burger)
    

    cv2.waitKey(1)
