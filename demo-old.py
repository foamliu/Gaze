#from gaze.nodes.core import EdgeDetection, AutoVideoSink, FaceDetection
from gaze.pipes import Graph
from gaze.nodes import VideoTestSource, FileSource, DefaultDeviceSource, NetworkSource, UdpSource
from gaze.nodes import FileSink, UdpSink, AutoVideoSink

x = UdpSource(port=5423)
#x = EdgeDetection()(x)
x = FileSink()(x)

graph = Graph(x)
graph.run()
