from .base_node import Node
from .source_node import SourceNode


class Sequential(Node):
    # Linear stack of layers.
    def __init__(self, nodes=None, name=None):
        super(Sequential, self).__init__(name=name)

        # Add to the model any layers passed to the constructor.
        if nodes:
            for node in nodes:
                self.add(node)

    @property
    def nodes(self):
        if self._nodes and isinstance(self._nodes[0], SourceNode):
            return self._nodes[1:]
        return self._nodes

    def add(self, node):
        if not isinstance(node, Node):
            raise TypeError('The added node must be '
                            'an instance of class Node. '
                            'Found: ' + str(node))
