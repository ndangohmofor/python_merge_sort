from math import inf
from heapq import heappop, heappush

def heuristic(start, target):
    x_distance = abs(start.position[0] - y.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return x_distance + y_distance


def a_star(graph, start, target):
    print("Starting A* Algorithm!")
    count = 0
    paths_and_distances = {}

    for vertex in graph:
        paths_and_distances[vertex] = [inf, [start.name]]

    paths_and_distances[start][0] = 0

    vertices_to_visit = [(0, start)]

    while vertices_to_visit and paths_and_distances[target][0] == inf:
        curr_dist, curr_vert = heappop(vertices_to_visit)
        for neigh, wgt in graph[curr_vert]:
            new_dist = curr_dist + wgt + heuristic(neigh, target)
            new_path = paths_and_distances[curr_vert][1] + [neigh.name]

            if new_dist < paths_and_distances[neigh][0]:
                paths_and_distances[neigh][0] = new_dist
                paths_and_distances[neigh][1] = new_path
                heappush(vertices_to_visit, (new_dist, neigh))
                count += 1
                print("At {0}".format(vertices_to_visit[0][1].name))

    print("Found a path in {0} steps: ".format(count), paths_and_distances[target][1])

    return paths_and_distances[target][1]
