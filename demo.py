from gaze.nodes import NetworkSource, VideoTestSource
from gaze.nodes.core import EdgeDetection, AutoVideoSink, FileSink
from gaze.pipes import Graph


if __name__ == '__main__':
    x = VideoTestSource()
    x = FileSink()(x)

    graph = Graph(x)
    graph.run()
