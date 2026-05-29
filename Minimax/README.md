# Minimax Algorithm for Tic-Tac-Toe

## Overview

This project implements the **Minimax Search Algorithm** in Python for the game of **Tic-Tac-Toe**. The program evaluates all possible future game states and determines the optimal outcome assuming both players play perfectly.


## Features

- Accepts a Tic-Tac-Toe board as user input.
- Uses the Minimax algorithm to recursively explore possible moves.
- Evaluates game states as:
  - **+1** : X wins
  - **-1** : O wins
  - **0** : Draw
- Determines the best achievable outcome for the player whose turn it is.

## How It Works

The Minimax algorithm treats Tic-Tac-Toe as a game tree:

- **Maximizing Player (X):** Attempts to maximize the score.
- **Minimizing Player (O):** Attempts to minimize the score.
- The algorithm recursively explores all legal moves until a terminal state (win, loss, or draw) is reached.
- Scores are propagated back through the game tree to determine the optimal result.

## Input Format

Enter the board as three rows using:

- `X` for X's moves
- `O` for O's moves
- `_` for empty cells

### Example

```text
X O X
_ O _
_ _ X
```

Then specify whose turn it is (`X` or `O`).


## Output

The program outputs the **Minimax score** representing the best possible outcome from the given board configuration.

### Score Interpretation

| Score | Meaning |
|---------|---------|
| +1 | X can force a win |
| 0 | Draw with optimal play |
| -1 | O can force a win |


## Applications

This implementation demonstrates fundamental concepts of:

- Adversarial Search
- Game Tree Exploration
- Artificial Intelligence Decision Making
- Recursive Algorithms and Backtracking
