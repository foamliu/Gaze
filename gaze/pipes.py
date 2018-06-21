from .engine.sequential import Sequential


class Graph(Sequential):
    def __init__(self, name=None):
        super(Graph, self).__init__(name=name)

    def run(self):
        pass
