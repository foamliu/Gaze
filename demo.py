from gaze.nodes import Source
from gaze.nodes.core import EdgeDetection, Sink
from gaze.pipes import Pipe

if __name__ == '__main__':
    x = Source()
    x = EdgeDetection()(x)
    x = Sink()(x)

    pipe = Pipe(x)
    pipe.run()
