import numpy as np
import cv2
import time
import urllib.request


def draw(boxes, frame):
    for (xA, yA, xB, yB) in boxes:
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                      (0, 255, 0), 2)
    print("no detected: {}\n\n".format(len(boxes)))


def read_photo(path: str, hog: object, maxsize: int = 500, quality: int = 2) -> object:
    req = urllib.request.urlopen(path)
    image_data = req.read()
    image_array = np.asarray(bytearray(image_data), dtype=np.uint8)
    frame = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    start = time.time()
    shape = frame.shape

    if shape[0] > maxsize or shape[1] > maxsize:
        if shape[0] > shape[1]:
            scale = maxsize/shape[0]
        else:
            scale = maxsize/shape[1]
        frame = cv2.resize(frame, (int(shape[1]*scale), int(shape[0]*scale)))

    mid = time.time()
    if quality == 1:
        boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8), scale=1.15, hitThreshold=0.1)
    if quality == 2:
        boxes, weights = hog.detectMultiScale(frame, winStride=(4, 4), scale=1.10, hitThreshold=0.1)
    if quality == 3:
        boxes, weights = hog.detectMultiScale(frame, winStride=(2, 2), scale=1.01, hitThreshold=0.1)
    end = time.time()
    print('time:\npreparation: {}\nanalysis: {}'.format(mid-start, end-mid))
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    draw(boxes, frame)
    return frame
