# src/astar.py
import heapq
import math
import time
from src.planner_base import PlannerBase, PlannerResult

def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

class AStarPlanner(PlannerBase):
    def __init__(self, grid, heuristic=manhattan):
        super().__init__(grid)
        self.heuristic = heuristic

    def plan(self, start, goal, dynamic_obstacles_at_time=None):
        t0 = time.time()
        frontier = []
        heapq.heappush(frontier, (0 + self.heuristic(start,goal), 0, start))
        came_from = {start: None}
        gscore = {start: 0}
        nodes_expanded = 0

        while frontier:
            f, g, current = heapq.heappop(frontier)
            nodes_expanded += 1
            if current == goal:
                break
            for n in self.grid.neighbors(current):
                tentative_g = gscore[current] + self.grid.cost(n)
                if n not in gscore or tentative_g < gscore[n]:
                    gscore[n] = tentative_g
                    priority = tentative_g + self.heuristic(n, goal)
                    heapq.heappush(frontier, (priority, tentative_g, n))
                    came_from[n] = current

        path = []
        if goal in came_from:
            cur = goal
            while cur:
                path.append(cur)
                cur = came_from[cur]
            path.reverse()
            total_cost = sum(self.grid.cost(c) for c in path)
        else:
            total_cost = float('inf')
        return PlannerResult(path, total_cost, nodes_expanded, time.time()-t0)
