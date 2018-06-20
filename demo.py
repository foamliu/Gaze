from gaze.nodes.core import Source, EdgeDetection, Sink

if __name__ == '__main__':
    x = Source()
    x = EdgeDetection()(x)
    x = Sink()(x)
