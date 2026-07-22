from queue import PriorityQueue

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}

pq = PriorityQueue()
visited = set()

pq.put((heuristic['A'], 'A'))

while not pq.empty():
    h, node = pq.get()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for i in graph[node]:
            pq.put((heuristic[i], i))
