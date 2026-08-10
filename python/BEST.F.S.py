import heapq

def best_first_search(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], start)]
    visited = set()
    parent = {start: None}

    while priority_queue:
        h, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(priority_queue,
                               (heuristic[neighbor], neighbor))

    # Construct path
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent.get(node)

    path.reverse()
    return path


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0
}

start = 'A'
goal = 'G'

path = best_first_search(graph, heuristic, start, goal)

print("Best First Search Path:")
print(" -> ".join(path))
