import json
from io import BytesIO

import cv2 as cv
import requests
from PIL import Image


def process_one_frame(image):
    detect_url = 'http://localhost:5000/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=true'

    image_file = BytesIO()
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    img = Image.fromarray(image_rgb)
    img.save(image_file, "JPEG")
    image_file.seek(0)

    files = [('images', ('test.jpg', image_file, 'image/jpeg'))]
    r = requests.post(detect_url, files=files)
    # print(r.text)
    face_boxes = json.loads(r.text)

    if len(face_boxes) > 0:
        return image
    else:
        return None
