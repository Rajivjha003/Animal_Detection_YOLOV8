from ultralytics import YOLO

# model
model = YOLO('yolov8.yaml')

# Training the model
results = model.train(data="E://Animal_Detection//config//config.yaml", epochs=20 ,imgsz=640)