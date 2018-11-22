from .base_node import Node
import cv2 as cv
import socket
import numpy as np


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
        self._cap = cv.VideoCapture(
            'videotestsrc pattern=snow ! video/x-raw,width=320,height=240 ! appsink sync=false ', 
            cv.CAP_GSTREAMER)

    def call(self, inputs=None, **kwargs):
        return self._cap.read()

class DefaultDeviceSource(SourceNode):
    def __init__(self, name=None):
        super(DefaultDeviceSource, self).__init__(name=name)
        self._cap = cv.VideoCapture(
            'autovideosrc ! decodebin ! videoconvert ! queue ! appsink sync=false',
            cv.CAP_GSTREAMER
        )
    def call(self, input=None, **kwargs):
        return self._cap.read()

class NetworkSource(SourceNode):
    def __init__(self, name=None):
        super(NetworkSource, self).__init__(name=name)
        self._cap = cv.VideoCapture(
            'udpsrc port=5423 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264  ! videoconvert  ! queue ! appsink sync=false ', 
            cv.CAP_GSTREAMER)

    def call(self, inputs=None, **kwargs):
        return self._cap.read()

class UdpSource(SourceNode):
    def __init__(self, ip="localhost", port=5001):
        super(UdpSource, self).__init__(name=None)
        self.UDP_HOST = ip
        self.UDP_PORT = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (self.UDP_HOST, self.UDP_PORT)
        self.sock.bind(server_address)
    
    def call(self, inputs=None, **kwargs):
        data, server = self.sock.recvfrom(65507)
        array = np.frombuffer(data, dtype=np.dtype('uint8'))
        img = cv.imdecode(array, 1)
        return True, img

class FileSource(SourceNode):
    def __init__(self, location):
        super(FileSource, self).__init__()
        command = 'filesrc location={} ! decodebin ! videoconvert ! queue ! appsink sync=false '.format(location)
        self._cap = cv.VideoCapture(command, cv.CAP_GSTREAMER)

    def call(self, inputs=None, **kwargs):
        return self._cap.read()
