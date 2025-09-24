# src/local_search.py
# Simple hill-climbing on path cost with random restarts. This is a hook to improve an existing path.
import random
from typing import List, Tuple

Cell = Tuple[int,int]

def perturb_path(path: List[Cell], grid, max_perturb=3):
    # randomly remove a small subpath and replan locally (naive)
    if len(path) < 4:
        return path
    i = random.randint(1, max(1, len(path)-3))
    j = min(len(path)-2, i + random.randint(1, max_perturb))
    new_path = path[:i] + path[j:]
    return new_path

def path_cost(path, grid):
    return sum(grid.cost(c) for c in path)

def hill_climb_improve(path, grid, iterations=100):
    best = path
    best_cost = path_cost(path, grid)
    for _ in range(iterations):
        cand = perturb_path(best, grid)
        # naive: accept if cost lower (in practice replan locally to fill gap)
        c_cost = path_cost(cand, grid)
        if c_cost < best_cost:
            best, best_cost = cand, c_cost
    return best
