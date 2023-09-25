def bfs(graph, start, target):
    path = [start]
    vertex_and_path = [start, path]

    search_queue = [vertex_and_path]

    visited = set()

    while search_queue:
        current, path = search_queue.pop(0)

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                if neighbor == target:
                    return path + [neighbor]
                else:
                    search_queue.append([neighbor, path + [neighbor]])


def dfs(graph, curr, target, visited = None):
    if visited is None:
        visited = []

    visited.append(curr)

    if curr == target:
        return visited

    for neighbor in graph[curr]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, target, visited)
            if path:
                return path
