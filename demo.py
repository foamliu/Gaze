from gaze.nodes import NetworkSource, VideoTestSource
from gaze.nodes.core import EdgeDetection, AutoVideoSink
from gaze.pipes import Graph


if __name__ == '__main__':
    x = VideoTestSource()
    x = EdgeDetection()(x)
    x = AutoVideoSink()(x)

    graph = Graph(x)
    graph.run()
