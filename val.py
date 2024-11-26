import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/trainlunwen/concrete-yolov8-chuantong-gaijin/weights/last.pt')
    model.val(data='dataset/mydata6-concrete-chuantong.yaml',
              split='val',
              imgsz=640,
              batch=16,
              rect=False,
              # save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='yolov8',
              )