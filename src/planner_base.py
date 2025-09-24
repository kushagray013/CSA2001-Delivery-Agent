# src/planner_base.py
import time
from typing import Tuple, List, Dict, Any

class PlannerResult:
    def __init__(self, path, cost, nodes_expanded, time_taken):
        self.path = path
        self.cost = cost
        self.nodes_expanded = nodes_expanded
        self.time_taken = time_taken

class PlannerBase:
    def __init__(self, grid):
        self.grid = grid
    
    def plan(self, start, goal, dynamic_obstacles_at_time=None):
        raise NotImplementedError
