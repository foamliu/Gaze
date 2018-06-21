from ..engine.base_node import Node


class EdgeDetection(Node):
    def __init__(self, **kwargs):
        super(EdgeDetection, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        return self


class Sink(Node):
    def __init__(self, **kwargs):
        super(Sink, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        return self


class AutoVideoSink(Sink):
    def __init__(self, **kwargs):
        super(AutoVideoSink, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        return self
