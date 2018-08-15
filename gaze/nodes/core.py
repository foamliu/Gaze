import cv2 as cv

from ..engine.base_node import Node


class EdgeDetection(Node):
    def __init__(self, **kwargs):
        super(EdgeDetection, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        gray = cv.cvtColor(inputs, cv.COLOR_BGR2GRAY)
        laplacian = cv.Laplacian(gray, cv.CV_8U)
        output = cv.cvtColor(laplacian, cv.COLOR_GRAY2RGB)
        return output


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


class FileSink(Sink):
    def __init__(self, **kwargs):
        super(FileSink, self).__init__(**kwargs)
        fourcc = cv.VideoWriter_fourcc(*'MPEG')
        self.out = cv.VideoWriter(filename='output.avi', fourcc=fourcc, fps=25.0, frameSize=(640, 360), isColor=True)

    def call(self, inputs, **kwargs):
        self.out.write(inputs)
        return None
