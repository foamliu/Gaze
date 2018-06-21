from gaze.nodes import VideoTestSource
from gaze.nodes.core import EdgeDetection, AutoVideoSink
from gaze.pipes import Graph
from gaze.utils import plot_graph

if __name__ == '__main__':
    x = VideoTestSource()
    x = EdgeDetection()(x)
    x = AutoVideoSink()(x)

    graph = Graph(x)
    graph.run()

    plot_graph(graph, to_file='model.svg')
