from .engine.base_node import Node
from .engine.sequential import Sequential


class Graph(Sequential):
    def __init__(self, node, name=None):
        if not isinstance(node, Node):
            raise TypeError('The added node must be '
                            'an instance of class Node. '
                            'Found: ' + str(node))
        super(Graph, self).__init__(node=node, name=name)

    def run(self):
        pass
