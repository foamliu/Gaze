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
        self._cap = cv.VideoCapture('videotestsrc ! appsink sync=false ', cv.CAP_GSTREAMER)

    def call(self, inputs=None, **kwargs):
        return self._cap.read()
