from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        print((x, y))

        if x == target or y == target:
            print("Target reached!")
            return

        q.extend([
            (jug1, y),          # Fill jug1
            (x, jug2),          # Fill jug2
            (0, y),             # Empty jug1
            (x, 0),             # Empty jug2
            (max(0, x-(jug2-y)), min(jug2, x+y)),  # Pour jug1 -> jug2
            (min(jug1, x+y), max(0, y-(jug1-x)))   # Pour jug2 -> jug1
        ])

water_jug(4, 3, 2)
