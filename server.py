from gaze.pipes import Graph
from gaze.nodes import VideoTestSource, FileSource, DefaultDeviceSource, NetworkSource, UdpSource
from gaze.nodes import FileSink, UdpSink, AutoVideoSink

x = UdpSource(port=5001,ip="0.0.0.0")
x = UdpSink(port=5001,ip="40.74.91.127")(x)

graph = Graph(x)
graph.run()
