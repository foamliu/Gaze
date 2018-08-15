from .base_node import Node
import cv2 as cv


class SourceNode(Node):
    # Node to be used as an entry point into a pipeline.
    def __init__(self, name=None):
        if not name:
            prefix = 'source'
            name = prefix + '_' + str(1)
        super(SourceNode, self).__init__(name=name)

    def call(self, inputs=None, **kwargs):
        return None


class VideoTestSource(SourceNode):
    def __init__(self, name=None):
        super(VideoTestSource, self).__init__(name=name)
        self._cap = cv.VideoCapture('videotestsrc ! video/x-raw-rgb, framerate=10/1, width=640, height=360 | appsink sync=false ', cv.CAP_GSTREAMER)

    def call(self, inputs=None, **kwargs):
        return self._cap.read()


class NetworkSource(SourceNode):
    def __init__(self, name=None):
        super(NetworkSource, self).__init__(name=name)
        self._cap = cv.VideoCapture('udpsrc port=5000 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264  ! videoconvert  ! queue ! appsink sync=false ', cv.CAP_GSTREAMER)

    def call(self, inputs=None, **kwargs):
        return self._cap.read()


class FileSource(SourceNode):
    def __init__(self, location):
        super(FileSource, self).__init__()
        command = 'filesrc location={} ! decodebin ! videoconvert ! queue ! appsink sync=false '.format(location)
        print(command)
        self._cap = cv.VideoCapture(command, cv.CAP_GSTREAMER)

    def call(self, inputs=None, **kwargs):
        return self._cap.read()
