

class Node(object):

    def __init__(self, **kwargs):
        self.built = False
        self._inbound_nodes = []
        self._outbound_nodes = []

        allowed_kwargs = {'input_shape',
                          'batch_size',
                          'dtype',
                          'name',
                          }
        for kwarg in kwargs:
            if kwarg not in allowed_kwargs:
                raise TypeError('Keyword argument not understood:', kwarg)

        name = kwargs.get('name')
        if not name:
            prefix = self.__class__.__name__
            name = prefix + '_' + str(123)
        self.name = name

    def call(self, inputs, **kwargs):
        return inputs

    def __call__(self, inputs, **kwargs):
        self.add_inbound_node(inputs)
        output = self.call(inputs, **kwargs)
        return output

    def build(self):
        self.built = True

    def add_inbound_node(self, input_tensors):
        self._inbound_nodes.append(input_tensors)

