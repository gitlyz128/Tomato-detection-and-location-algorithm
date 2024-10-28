import torch
import cv2




# model = torch.hub.load("./","custom",path = "best.pt",source="local")
#
#
# cap= cv2.VideoCapture(0)
# while (1):
#    ret, frame = cap . read()
#    results = model(frame)
#
#    results.show()
#
#     # img = "./data/tomato_image/left_1.jpg"

# pip install "C:\Users\shuai\Desktop\TensorRT-8.5.3.1.Windows10.x86_64.cuda-11.8.cudnn8.6\TensorRT-8.5.3.1\python\tensorrt-8.5.3.1-cp38-none-win_amd64.whl"
# pip install onnx

# python export.py --weights best.pt --include engine --device 0  --imgsz 192 320 --half
#pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.10.0-f https://download.pytorch.org/whl/torch_stable.html
