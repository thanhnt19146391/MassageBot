import os
import cv2
import numpy as np

FOLDER = './yolov3/'
WEIGHT_FILEPATH = FOLDER + 'yolov3_training_last.weights' 
CFG_FILEPATH = FOLDER + 'yolov3_testing.cfg'
CLASSES_FILEPATH = FOLDER + "classes.txt"
FONT = cv2.FONT_HERSHEY_PLAIN
TEST_FOLDER = FOLDER + 'test_images'


# Read classes
classes = []
with open(CLASSES_FILEPATH, "r") as f:
    classes = f.read().splitlines()

# Load net
net = cv2.dnn.readNet(WEIGHT_FILEPATH, CFG_FILEPATH)

for _, filePath in enumerate(os.listdir(TEST_FOLDER)):
    img = cv2.imread(filePath)
    height, width, _ = img.shape
    if height < width:
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        height, width, _ = img.shape
    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)
    boxes = []
    confidences = []
    class_ids = []
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.2:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)

    if len(indexes)>0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i],2))
            color = (0, 0, 0)
            cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
            cv2.putText(img, label + " " + confidence, (x, y+20), FONT, 1, (255,255,255), 2)

    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key==27:
        break

cv2.destroyAllWindows()