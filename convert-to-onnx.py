from ultralytics import YOLO

m = YOLO("yolov7_training.pt")
m.export(format="onnx", imgsz=[384, 640])
