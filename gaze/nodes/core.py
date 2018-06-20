from ..engine.base_node import Node


class Source(Node):
    def __init__(self, **kwargs):
        super(Source, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        return inputs


class EdgeDetection(Node):
    def __init__(self, **kwargs):
        super(EdgeDetection, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        return inputs


class Sink(Node):
    def __init__(self, **kwargs):
        super(Sink, self).__init__(**kwargs)

    def call(self, inputs, **kwargs):
        return inputs
