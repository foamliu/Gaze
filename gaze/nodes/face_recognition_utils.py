import json
from io import BytesIO

import cv2 as cv
import requests
from PIL import Image


def get_personId_name_mappings():
    name2personId = dict()
    name2personId['a-yuhu'] = 'f1dfd6a7-85e4-4b83-94ea-63ae96e6bf6a'
    name2personId['abelch'] = 'e2c15b40-7d7b-4372-97cc-206a53840085'
    name2personId['bekimd'] = '5db152bb-9ca3-43a1-9d29-95781324b6c9'
    name2personId['eridai'] = 'f35752b9-eef5-4108-8fe1-7e764ebbec2a'
    name2personId['fanzhang'] = '44d34724-7ba7-4ab8-897a-612770700f74'
    name2personId['foamliu'] = '4dd7401a-86a8-48ed-bdf8-c1dc861e07d0'
    name2personId['georgel'] = '6d6a711b-04d0-4f33-ba5a-bdd61d711ea0'
    name2personId['guanghu'] = 'e2332abd-c74f-45cc-87bf-46532b50875a'
    name2personId['jiahan'] = '85148c06-c2ed-465f-aa98-b490e22c62da'
    name2personId['jifwang'] = 'cc71e813-c29a-42de-bee3-c9e28b0b2074'
    name2personId['jusjin'] = 'bb8d4910-1c4f-4534-9940-72c094a60193'
    name2personId['justisun'] = '5f271115-ec1f-4ee7-a6c0-51b864e3b6c1'
    name2personId['quying'] = '271616a1-e9a5-4d2c-ab76-5e87a424410a'
    name2personId['rbao'] = '710f9a38-804c-442a-a93b-4375e38cbb01'
    name2personId['shengl'] = '3563d210-4ef5-41b8-bda8-e146910a75f9'
    name2personId['xiaofmao'] = '8c1ead3b-361b-4948-a3a4-c29b0bf92b0b'
    name2personId['xiaotl'] = '451ee7f3-5628-41d6-9b99-33e15da8697e'

    personId2name = dict()
    for key in name2personId.keys():
        personId2name[name2personId[key]] = key

    return personId2name, name2personId


personId2name, name2personId = get_personId_name_mappings()


def draw_boxes(image, faceRectangle, name):
    xmin = faceRectangle['left']
    ymin = faceRectangle['top']
    width = faceRectangle['width']
    height = faceRectangle['height']
    pt1 = (xmin, ymin)
    pt2 = (xmin + width, ymin + height)
    cv.rectangle(image, pt1, pt2, (0, 255, 0), 1)
    cv.putText(image, name, (xmin + 1, ymin + 1), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), thickness=2, lineType=cv.LINE_AA)
    cv.putText(image, name, (xmin, ymin), cv.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), lineType=cv.LINE_AA)


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

    faceId_list = []
    for face in face_boxes:
        faceId_list.append(face['faceId'])

    # print(len(faceId_list))
    # print(faceId_list)

    req = {
        "largePersonGroupId": "64b300c6-b4c4-11e8-878e-d89ef339b7b0",
        "faceIds": faceId_list,
        "maxNumOfCandidatesReturned": 3,
        "confidenceThreshold": 0.5
    }
    identify_url = 'http://localhost:5000/face/v1.0/identify'
    r = requests.post(identify_url, json=req)
    # print(r.text)

    face_identities = json.loads(r.text)
    for face in face_identities:
        if face['candidates']:
            faceId = face['faceId']
            personId = face['candidates'][0]['personId']
            name = personId2name[personId]
            faceRectangle = [f['faceRectangle'] for f in face_boxes if f['faceId'] == faceId][0]
            # print(name)
            # print(faceRectangle)
            draw_boxes(image, faceRectangle, name)

    return image
