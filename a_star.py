import heapq
from math import inf
from vertex import Vertex


def a_star(graph, start, end):
    paths_and_distances = {}
    for vertex in graph:
        paths_and_distances[vertex] = [inf, [start.name]]
    paths_and_distances[start][0] = 0

    vertices_to_explore = [(0, start)]

    while vertices_to_explore:
        curr_dist, curr_vert = heapq.heappop(vertices_to_explore)
        for neighbor, edge_weight in graph[curr_vert]:
            new_dist = curr_dist + edge_weight
            new_path = paths_and_distances[curr_vert][1] + [neighbor.name]
            if new_dist < paths_and_distances[neighbor][0]:
                paths_and_distances[neighbor][0] = new_dist
                paths_and_distances[neighbor][1] = new_path
                heapq.heappush(vertices_to_explore, neighbor)
    return paths_and_distances[end][1]
