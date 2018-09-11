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


class FaceDetection(Node):
    def __init__(self, **kwargs):
        super(FaceDetection, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        from ..nodes.face_detection_utils import process_one_frame
        return process_one_frame(inputs)


class FaceRecognition(Node):
    def __init__(self, **kwargs):
        super(FaceRecognition, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        from ..nodes.face_recognition_utils import process_one_frame
        return process_one_frame(inputs)


class Sink(Node):
    def __init__(self, **kwargs):
        super(Sink, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        return self


class AutoVideoSink(Sink):
    def __init__(self, **kwargs):
        super(AutoVideoSink, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        if inputs is not None:
            cv.imshow('AutoVideoSink', inputs)
        return None


class FileSink(Sink):
    def __init__(self, **kwargs):
        super(FileSink, self).__init__(**kwargs)
        fourcc = cv.VideoWriter_fourcc(*'MPEG')
        self.out = cv.VideoWriter(filename='output.avi', fourcc=fourcc, fps=20.0, frameSize=(960, 720), isColor=True)

    def call(self, inputs, **kwargs):
        if inputs is not None:
            self.out.write(inputs)
        return None
