import json
import onnx

model = onnx.load('yolov7_training.onnx')

names = ['Lettuce', 'Onion', 'Pickle', 'Tomato']

m1 = model.metadata_props.add()
m1.key = "names"
m1.value = json.dumps(names)

onnx.save(model, 'yolov7_training.onnx')
