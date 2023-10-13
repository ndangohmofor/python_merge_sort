import heapq
from math import inf
from vertex import Vertex


def a_star(graph, start: Vertex):
    distances = {}
    for vertex in graph:
        distances[vertex] = inf
    distances[start] = 0

    vertices_to_explore = [(0, start)]

    while vertices_to_explore:
        curr_dist, curr_vert = heapq.heappop(vertices_to_explore)
        for neighbor, edge_weight in graph[curr_vert]:
            new_dist = curr_dist + edge_weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(vertices_to_explore, neighbor)
    return distances
