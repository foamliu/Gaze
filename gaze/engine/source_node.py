from .base_node import Node


class SourceNode(Node):
    # Node to be used as an entry point into a pipeline.
    def __init__(self, name=None):
        if not name:
            prefix = 'source'
            name = prefix + '_' + str(1234)
        super(SourceNode, self).__init__(name=name)


def Source():
    source_node = SourceNode()
    return source_node
