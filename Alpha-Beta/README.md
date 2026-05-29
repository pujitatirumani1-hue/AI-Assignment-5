# Alpha-Beta Pruning Algorithm

## Overview

This project implements the **Alpha-Beta Pruning Algorithm** in Python. It is an optimization of the Minimax algorithm that reduces the number of nodes evaluated in a game tree while still producing the same optimal result.


## Features

- Accepts the depth of a complete binary game tree as user input.
- Accepts leaf node values from the user.
- Uses Alpha-Beta Pruning to evaluate the game tree.
- Simulates alternating Maximizing and Minimizing players.
- Prunes branches that cannot affect the final decision.
- Returns the optimal value for the root node.


## How It Works

The Alpha-Beta algorithm explores a game tree recursively:

- **Maximizing Player:** Chooses the highest value.
- **Minimizing Player:** Chooses the lowest value.
- **Alpha (α):** Best value found so far for the maximizing player.
- **Beta (β):** Best value found so far for the minimizing player.

When **β ≤ α**, further exploration of that branch is unnecessary and is skipped (**pruned**).

This reduces computation while producing the same result as Minimax.


## Input Format

1. Enter the depth of the binary tree.
2. Enter the leaf node values separated by spaces.

### Example Input

```text
Enter tree depth: 3
Enter 8 leaf node values:
3 5 6 9 1 2 0 -1
```

### Example Output

```text
Best value: 5
```


## Applications

This implementation demonstrates fundamental concepts of:

- Alpha-Beta Pruning
- Adversarial Search
- Game Tree Evaluation
- Artificial Intelligence Decision Making
- Recursive Algorithms
- Optimization of Minimax Search


## Advantages of Alpha-Beta Pruning

- Produces the same result as Minimax.
- Evaluates fewer nodes.
- Improves search efficiency.
- Enables deeper game-tree exploration within the same time limit.
