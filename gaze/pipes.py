from .engine.base_node import Node
from .engine.sequential import Sequential


def traverse(nodes, node):
    for sub_node in node._inbound_nodes:
        nodes.append(sub_node)
        traverse(nodes, sub_node)


class Graph(Sequential):
    def __init__(self, node, name=None):
        if not isinstance(node, Node):
            raise TypeError('The added node must be '
                            'an instance of class Node. '
                            'Found: ' + str(node))

        nodes = []
        traverse(nodes, node)

        super(Graph, self).__init__(nodes=nodes, name=name)

    def run(self):
        pass
