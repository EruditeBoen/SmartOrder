#!/bin/bash

mkdir resources
cd resources
curl "https://s3.ap-northeast-2.wasabisys.com/pinto-model-zoo/307_YOLOv7/no-postprocess/resources.tar.gz" -o resources.tar.gz
tar -zxvf resources.tar.gz
rm resources.tar.gz
cd ../models
cp ../resources/yolov7_384x640.onnx .
cd ../
rm -rf resources

echo Download finished.
