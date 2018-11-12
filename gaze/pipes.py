from .engine.base_node import Node
from .engine.sequential import Sequential
import cv2 as cv


class Graph(Sequential):
    def __init__(self, node, name=None):
        if not isinstance(node, Node):
            raise TypeError('The added node must be '
                            'an instance of class Node. '
                            'Found: ' + str(node))
        super(Graph, self).__init__(node=node, name=name)
        self._output = node

    def run(self):
        source = self._nodes[0]

        while True:
            ret, frame = source.call()
            if ret == True:
                for node in self._nodes[1:]:
                    frame = node.call(frame)

                ch = cv.waitKey(1)
                if ch == 27:
                    break
            else:
                break

