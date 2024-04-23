# Algorithm Design and Analysis: Traveling Salesman Problem

## Overview

This project implements solutions to the Traveling Salesman Problem (TSP), a classic combinatorial optimization problem in computer science. The TSP seeks to find the shortest possible route that visits each city exactly once and returns to the original city.

## Algorithms and Techniques

The project implements and compares the following algorithms:

1. **Brute Force:** Exhaustively generates all possible permutations of routes and selects the one with the shortest total distance. Suitable for small to moderate-sized instances.
2. **Greedy Algorithm:** Uses the Nearest Neighbor heuristic to select the closest unvisited city at each step. Prioritizes efficiency over optimality.
3. **Dynamic Programming (Held-Karp Algorithm):** Breaks down the problem into smaller subproblems and gradually builds up to the full tour, leveraging memorization to avoid redundant computations.

## References

Hoffman, K. L., Padberg, M., & Rinaldi, G. (2013). Traveling salesman problem. Encyclopedia of Operations Research and Management Science, 1, 1573-1578.

