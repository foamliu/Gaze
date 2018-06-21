import os

import pydot


def graph_to_dot(graph,
                 show_shapes=False,
                 show_node_names=True):
    from ..nodes.wrappers import Wrapper
    from ..pipes import Sequential

    dot = pydot.Dot()
    dot.set('concentrate', True)
    dot.set_node_defaults(shape='record')

    if isinstance(graph, Sequential):
        if not graph.built:
            graph.build()
    nodes = graph.nodes
    print('len(nodes): ' + str(len(nodes)))

    # Create graph nodes.
    for node in nodes:
        node_id = str(id(node))

        # Append a wrapped layer's label to node's label, if it exists.
        node_name = node.name
        class_name = node.__class__.__name__
        if isinstance(node, Wrapper):
            node_name = '{}({})'.format(node_name, node.layer.name)
            child_class_name = node.layer.__class__.__name__
            class_name = '{}({})'.format(class_name, child_class_name)

        # Create node's label.
        if show_node_names:
            label = '{}: {}'.format(node_name, class_name)
        else:
            label = class_name

        # Rebuild the label as a table including input/output shapes.
        if show_shapes:
            try:
                outputlabels = str(node.output_shape)
            except AttributeError:
                outputlabels = 'multiple'
            if hasattr(node, 'input_shape'):
                inputlabels = str(node.input_shape)
            elif hasattr(node, 'input_shapes'):
                inputlabels = ', '.join(
                    [str(ishape) for ishape in node.input_shapes])
            else:
                inputlabels = 'multiple'
            label = '%s\n|{input:|output:}|{{%s}|{%s}}' % (label,
                                                           inputlabels,
                                                           outputlabels)
        node = pydot.Node(node_id, label=label)
        dot.add_node(node)

    # Connect nodes with edges.
    for node in nodes:
        node_id = str(id(node))
        for i, node in enumerate(node._inbound_nodes):
            node_key = node.name + '_ib-' + str(i)
            if node_key in graph._network_nodes:
                for inbound_layer in node.inbound_layers:
                    inbound_layer_id = str(id(inbound_layer))
                    node_id = str(id(node))
                    dot.add_edge(pydot.Edge(inbound_layer_id, node_id))
    return dot


def plot_graph(graph,
               to_file='model.png',
               show_shapes=False,
               show_node_names=True):
    dot = graph_to_dot(graph, show_shapes, show_node_names)
    _, extension = os.path.splitext(to_file)
    if not extension:
        extension = 'png'
    else:
        extension = extension[1:]
    dot.write(to_file, format=extension)
