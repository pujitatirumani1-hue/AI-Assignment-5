import random

def monte_carlo(values, simulations):
    best_score = float('-inf')

    for value in values:
        score = 0

        for _ in range(simulations):
            score += value + random.randint(-2, 2)

        avg_score = score / simulations
        best_score = max(best_score, avg_score)

    return best_score

n = int(input("Enter number of moves: "))
values = list(map(int, input("Enter move values: ").split()))
simulations = int(input("Enter number of simulations: "))

result = monte_carlo(values, simulations)

print("Best estimated value:", round(result, 2))
