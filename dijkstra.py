from heapq import heappop, heappush
from math import inf

graph = {
    'A': [('B', 10), ('C', 3)],
    'C': [('D', 2)],
    'D': [('E', 10)],
    'E': [],
    'B': [('C', 3), ('D', 2)]
}
