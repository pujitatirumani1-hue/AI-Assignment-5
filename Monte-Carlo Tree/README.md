# Monte Carlo Search Algorithm

## Overview

This project implements a simple **Monte Carlo Search Algorithm** in Python. The algorithm estimates the value of different moves by running multiple random simulations and selecting the move with the highest average score.

## Features

- Accepts a list of move values as user input.
- Accepts the number of simulations to perform.
- Uses random sampling to estimate move quality.
- Calculates the average score for each move over multiple simulations.
- Selects the move with the highest estimated value.
- Demonstrates the basic idea behind Monte Carlo methods used in Artificial Intelligence.

## How It Works

The Monte Carlo algorithm evaluates each move through repeated random simulations:

1. Each move starts with a predefined value.
2. A random number between **-2 and 2** is added during every simulation.
3. The scores from all simulations are accumulated.
4. The average score is calculated for each move.
5. The move with the highest average score is chosen as the best estimated move.

Because randomness is involved, results may vary slightly between executions.

## Input Format

1. Enter the number of moves.
2. Enter the move values separated by spaces.
3. Enter the number of simulations.

## Example

### Input

```text
Enter number of moves: 4
Enter move values: 3 5 2 7
Enter number of simulations: 1000
```

### Output

```text
Best estimated value: 7.03
```

*The exact value may vary because of random simulations.*

## Applications

This implementation demonstrates fundamental concepts of:

- Monte Carlo Search
- Random Sampling
- Probabilistic Decision Making
- Artificial Intelligence
- Simulation-Based Evaluation
- Approximate Search Algorithms

## Advantages of Monte Carlo Search

- Simple and easy to implement.
- Handles uncertainty through random simulations.
- Can estimate good decisions without exploring all possibilities.
- Useful for large search spaces where exhaustive search is impractical.
- Forms the foundation of more advanced techniques such as **Monte Carlo Tree Search (MCTS)**.
