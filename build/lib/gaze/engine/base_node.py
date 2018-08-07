import re


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
            name = _to_snake_case(prefix) + '_' + str(1)
        self.name = name

    def call(self, inputs, **kwargs):
        return inputs

    def __call__(self, node, inputs=None, **kwargs):
        # print('__call__ inputs: ' + str(inputs))
        self._add_inbound_node(node)
        return self

    def build(self):
        self.built = True

    def _add_inbound_node(self, input_tensors):
        self._inbound_nodes.append(input_tensors)


def _to_snake_case(name):
    intermediate = re.sub('(.)([A-Z][a-z0-9]+)', r'\1_\2', name)
    insecure = re.sub('([a-z])([A-Z])', r'\1_\2', intermediate).lower()
    # If the class is private the name starts with "_" which is not secure
    # for creating scopes. We prefix the name with "private" in this case.
    if insecure[0] != '_':
        return insecure
    return 'private' + insecure
