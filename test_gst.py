import time

import cv2 as cv

cap = cv.VideoCapture(
    'udpsrc port=5000 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264  ! videoconvert  ! queue ! appsink sync=false',
    cv.CAP_GSTREAMER)

start = time.time()
frame_id = 0
# capture frames from the camera
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # show the frame
    cv.imshow("Frame", frame)
    key = cv.waitKey(1) & 0xFF

    start = time.time()
    frame_id += 1

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
