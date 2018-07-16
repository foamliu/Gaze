from gaze.nodes import FileSource
from gaze.nodes.core import EdgeDetection, AutoVideoSink
from gaze.pipes import Graph

if __name__ == '__main__':
    x = FileSource('~/code/Gaze/movie.mp4')
    x = EdgeDetection()(x)
    x = AutoVideoSink()(x)

    graph = Graph(x)
    graph.run()
