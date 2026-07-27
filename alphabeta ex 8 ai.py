def alphabeta(depth, nodeIndex, isMax, values, alpha, beta):

    if depth == 2:
        return values[nodeIndex]

    if isMax:
        best = -1000
        for i in range(2):
            best = max(best, alphabeta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 1000
        for i in range(2):
            best = min(best, alphabeta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 2, 9]
print("Optimal Value:", alphabeta(0, 0, True, values, -1000, 1000))
