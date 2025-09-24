# src/bfs.py
from collections import deque
from src.planner_base import PlannerBase, PlannerResult
import time

class BFSPlanner(PlannerBase):
    def plan(self, start, goal, dynamic_obstacles_at_time=None):
        start_time = time.time()
        frontier = deque([start])
        came_from = {start: None}
        nodes_expanded = 0

        while frontier:
            current = frontier.popleft()
            nodes_expanded += 1
            if current == goal:
                break
            for n in self.grid.neighbors(current):
                if n not in came_from:
                    came_from[n] = current
                    frontier.append(n)
        # reconstruct
        path = []
        if goal in came_from:
            cur = goal
            while cur:
                path.append(cur)
                cur = came_from[cur]
            path.reverse()
            cost = sum(self.grid.cost(c) for c in path)
        else:
            cost = float('inf')
            path = []
        return PlannerResult(path, cost, nodes_expanded, time.time()-start_time)
