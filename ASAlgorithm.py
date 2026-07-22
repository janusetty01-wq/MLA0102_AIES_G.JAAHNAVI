import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 2,
    'E': 1,
    'F': 0
}

pq = [(heuristic['A'], 0, 'A')]
visited = set()

while pq:
    f, g, node = heapq.heappop(pq)
    if node not in visited:
        print(node, "Cost:", g)
        visited.add(node)
        for n, c in graph[node]:
            heapq.heappush(pq, (g + c + heuristic[n], g + c, n))
