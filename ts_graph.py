from ts_vertex import Vertex


class Graph:
    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex: Vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight: int = 0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex: Vertex, end_vertex: Vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            curr_vertex = start.pop(0)
            seen[curr_vertex] = True
            print("Visiting {0}".format(curr_vertex))
            if curr_vertex == end_vertex:
                return True
            else:
                vertices_to_visit = set(self.graph_dict[curr_vertex].edges.keys())
                start += [vertex for vertex in vertices_to_visit if vertex not in seen]
        return False