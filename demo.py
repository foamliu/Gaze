
from gaze.nodes import NetworkSource, VideoTestSource, NetworkSource
from gaze.nodes.core import EdgeDetection, FaceRecognition, AutoVideoSink, FileSink
from gaze.pipes import Graph


if __name__ == '__main__':
    x = NetworkSource()
    x = FaceRecognition()(x)
    x = FileSink()(x)

    graph = Graph(x)
    graph.run()
