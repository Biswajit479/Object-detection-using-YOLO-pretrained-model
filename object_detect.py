from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np

class detection:
    # define the model
    def __init__(self):
        self.model = YOLO('yolo11m.pt')
    
    def obj_detect(self, file):
        # convert uplod file into PIL
        image = Image.open(file).convert("RGB")
        
        # convert PIL -> numpy array
        img = np.array(image)
        
        # detect the object
        result = self.model(img)
        
        # Get ploted image using Bounding Box
        annotated_image = result[0].plot()
        
        # Convert BGR color to RGB
        annotated_img = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
        
        return annotated_image