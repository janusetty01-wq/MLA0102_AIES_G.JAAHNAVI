from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

def ucs(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start, [start]))
    visited = set()

    while not pq.empty():
        cost, node, path = pq.get()

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", cost)
            return

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    pq.put((cost + weight, neighbor, path + [neighbor]))

ucs(graph, 'A', 'F')
