import heapq

def a_star(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, cost

        for neighbor, distance in graph[node]:
            if neighbor not in visited:
                new_cost = cost + distance
                new_f = new_cost + heuristic[neighbor]
                heapq.heappush(
                    pq,
                    (new_f, new_cost, neighbor, path + [neighbor])
                )

    return None, None


graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3), ('G', 2)],
    'G': [('D', 2)]
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'G': 0
}

path, cost = a_star(graph, heuristic, 'A', 'G')

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)
