

class Node(object):

    def __init__(self, **kwargs):
        pass

    def call(self, inputs, **kwargs):
        return inputs

    def __call__(self, inputs, **kwargs):
        output = self.call(inputs, **kwargs)
        return output

