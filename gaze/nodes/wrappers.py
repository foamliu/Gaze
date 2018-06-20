from ..engine.base_node import Node


class Wrapper(Node):
    def __init__(self, node, **kwargs):
        self.layer = node
        super(Wrapper, self).__init__(**kwargs)
