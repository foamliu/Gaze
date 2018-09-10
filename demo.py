from gaze.nodes import NetworkSource, VideoTestSource, FileSource
from gaze.nodes.core import EdgeDetection, AutoVideoSink, FaceRecognition
from gaze.pipes import Graph


if __name__ == '__main__':
    x = NetworkSource()
    x = FaceRecognition()(x)
    x = AutoVideoSink()(x)

    graph = Graph(x)
    graph.run()
