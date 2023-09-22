def bfs(graph, start_vertex, target_value):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]

    bfs_queue = [vertex_and_path]

    visited = {}