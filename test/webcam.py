from gaze.pipes import Graph
from gaze.nodes import VideoTestSource, FileSource, DefaultDeviceSource, NetworkSource, UdpSource
from gaze.nodes import FileSink, UdpSink, AutoVideoSink
from gaze.nodes.core import EdgeDetection

x = DefaultDeviceSource()
x = UdpSink(ip="52.231.153.185", port=5001)(x)
#x = UdpSink(ip="10.94.192.228", port=5423)(x)

graph = Graph(x)
graph.run()