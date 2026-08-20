def minimax(depth, nodeIndex, isMax, values):

    if depth == 2:
        return values[nodeIndex]

    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values)
        )

values = [3, 5, 2, 9]
print("Optimal Value:", minimax(0, 0, True, values))
