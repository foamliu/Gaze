from gaze.pipes import Graph
from gaze.nodes import VideoTestSource, FileSource, DefaultDeviceSource, NetworkSource, UdpSource
from gaze.nodes import FileSink, UdpSink, AutoVideoSink

#x = DefaultDeviceSource()
#x = UdpSink( port=5001)(x)
#x = UdpSource(ip="0.0.0.0",port=5001)(x)
#x = AutoVideoSink()(x)

x = VideoTestSource()
x = FileSink()(x)

graph = Graph(x)
graph.run()