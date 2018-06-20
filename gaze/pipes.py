from .engine.sequential import Sequential


class Pipe(Sequential):
    def __init__(self, name=None):
        super(Pipe, self).__init__(name=name)

    def run(self):
        pass
