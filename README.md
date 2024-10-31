# Important
- Make sure you have a webcam!
  
# Requirements

 * Library requirements are already installed in the bobo venv
 * Linux based shell
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
```

# Credit:
* YOLOv7 model: [https://github.com/PINTO0309/PINTO_model_zoo/tree/main/307_YOLOv7]
* ibaiGorordo: [https://github.com/ibaiGorordo/ONNX-YOLOv7-Object-Detection/tree/main]

