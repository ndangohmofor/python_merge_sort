from math import inf
from heapq import heappop, heappush
from manhattan_graph import manhattan_graph, thirty_sixth_and_sixth, grand_central_station


def modified_dijkstra(graph, start, target):
    count = 0
    path_and_distance = {}

    for vertex in graph:
        path_and_distance[vertex] = [inf, [start.name]]

    path_and_distance[start][0] = 0

    vertices_to_visit = [(0, start)]

    while vertices_to_visit:
        curr_dist, curr_vert = heappop(vertices_to_visit)

        for neigh, weight in graph[curr_vert]:
            new_dist = curr_dist + weight
            new_path = path_and_distance[curr_vert][1] + [neigh.name]

            if new_dist < path_and_distance[neigh][0]:
                path_and_distance[neigh][0] = new_dist
                path_and_distance[neigh][1] = new_path
                heappush(vertices_to_visit, (new_dist, neigh))
                count += 1
                print("At {0}\n".format(vertices_to_visit[0][1].name) )
    print("Found a path in {0} steps: ".format(count), path_and_distance[target][1])
    return path_and_distance[target][1]


modified_dijkstra(manhattan_graph, thirty_sixth_and_sixth, grand_central_station)