from ..engine.base_node import Node
import cv2 as cv


class EdgeDetection(Node):
    def __init__(self, **kwargs):
        super(EdgeDetection, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        gray = cv.cvtColor(inputs, cv.COLOR_BGR2GRAY)
        laplacian = cv.Laplacian(gray, cv.CV_8U)
        return laplacian


class Sink(Node):
    def __init__(self, **kwargs):
        super(Sink, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        return self


class AutoVideoSink(Sink):
    def __init__(self, **kwargs):
        super(AutoVideoSink, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        cv.imshow('AutoVideoSink', inputs)
        return None
