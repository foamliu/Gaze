import numpy as np
import cv2

videoFilePath = "movie.mp4"
#cap =cv2.VideoCapture(videoFilePath) 
cap = cv2.VideoCapture(
    'filesrc location=movie.mp4 ! decodebin ! videoconvert ! queue ! appsink sync=false ',
    cv2.CAP_GSTREAMER)

frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, 20, (frame_width, frame_height)) 


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)
        #print(np.shape(frame))
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()