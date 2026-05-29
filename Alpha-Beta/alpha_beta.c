import math

def alphabeta(depth, node, maximizing, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node]

    if maximizing:
        best = -math.inf
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i,
                            False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i,
                            True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


depth = int(input("Enter tree depth: "))
n = 2 ** depth

print(f"Enter {n} leaf node values:")
values = list(map(int, input().split()))

result = alphabeta(0, 0, True, values,
                   -math.inf, math.inf, depth)

print("Best value:", result)
