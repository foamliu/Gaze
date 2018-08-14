from gaze.nodes import NetworkSource
from gaze.nodes.core import EdgeDetection, AutoVideoSink
from gaze.pipes import Graph


if __name__ == '__main__':
    x = NetworkSource()
    x = AutoVideoSink()(x)

    graph = Graph(x)
    graph.run()
