from .base_node import Node


class Sequential(Node):
    def __init__(self, node=None, name=None):
        super(Sequential, self).__init__(name=name)

        self._nodes = []

        if node:
            self.add(node)

        self._nodes.reverse()

    def add(self, node):
        # print('add node: ' + str(node))
        if not isinstance(node, Node):
            raise TypeError('The added node must be '
                            'an instance of class Node. '
                            'Found: ' + str(node))

        self._nodes.append(node)
        for sub_node in node._inbound_nodes:
            self.add(sub_node)
