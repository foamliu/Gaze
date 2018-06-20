from gaze.nodes.core import EdgeDetection, Sink
from gaze.nodes import Source

if __name__ == '__main__':
    x = Source()
    x = EdgeDetection()(x)
    x = Sink()(x)
