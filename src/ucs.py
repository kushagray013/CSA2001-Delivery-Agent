# src/ucs.py
import heapq
from src.planner_base import PlannerBase, PlannerResult
import time

class UCSPlanner(PlannerBase):
    def plan(self, start, goal, dynamic_obstacles_at_time=None):
        t0 = time.time()
        frontier = []
        heapq.heappush(frontier, (0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}
        nodes_expanded = 0

        while frontier:
            cost, current = heapq.heappop(frontier)
            nodes_expanded += 1
            if current == goal:
                break
            for n in self.grid.neighbors(current):
                new_cost = cost_so_far[current] + self.grid.cost(n)
                if n not in cost_so_far or new_cost < cost_so_far[n]:
                    cost_so_far[n] = new_cost
                    heapq.heappush(frontier, (new_cost, n))
                    came_from[n] = current
        path = []
        if goal in came_from:
            cur = goal
            while cur:
                path.append(cur)
                cur = came_from[cur]
            path.reverse()
            total_cost = cost_so_far[goal]
        else:
            total_cost = float('inf')
        return PlannerResult(path, total_cost, nodes_expanded, time.time()-t0)
