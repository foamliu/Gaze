from gaze.nodes.core import EdgeDetection, AutoVideoSink
from gaze.pipes import Graph
from gaze.nodes import VideoTestSource
x = VideoTestSource()
x = EdgeDetection()(x)
x = AutoVideoSink()(x)
graph = Graph(x)
graph.run()
