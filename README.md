# Important
- Make sure you have a webcam!
  
# Requirements

 * Library requirements are already installed in the bobo venv
 * Python3.8 reccomended

# Installation
```shell
git clone https://github.com/EruditeBoen/SmartOrder.git
cd SmartOrder
source bobo/bin/activate
./download_model.sh
```
If you get a permission when running the shell script:
```shell
chmod -R 777
```
Feel free to take a look at the script if you are skeptical.
```shell
nano ./download_model.sh
```

### ONNX Runtime
For Nvidia GPU computers:
`pip install onnxruntime-gpu`

Otherwise:
`pip install onnxruntime`

# Example

 * **Image inference**:
 ```shell
 python Order.py

# References:
* YOLOv8 model: [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)
* YOLOv5 model: [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
* YOLOv6 model: [https://github.com/meituan/YOLOv6](https://github.com/meituan/YOLOv6)
* YOLOv7 model: [https://github.com/WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7)
* PINTO0309's model zoo: [https://github.com/PINTO0309/PINTO_model_zoo](https://github.com/PINTO0309/PINTO_model_zoo)
* PINTO0309's model conversion tool: [https://github.com/PINTO0309/openvino2tensorflow](https://github.com/PINTO0309/openvino2tensorflow)
