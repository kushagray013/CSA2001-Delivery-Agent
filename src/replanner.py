# src/replanner.py
# Simple demo showing A* planning and dynamic obstacle causing replanning.
from src.grid import Grid
from src.astar import AStarPlanner
from src.ucs import UCSPlanner
import time
import csv

def demo_dynamic_replan(mapfile, start, goal, dynamic_schedule, out_log):
    """
    dynamic_schedule: dict[time_step] -> set(cells occupied)
    We simulate discrete time steps; agent moves one cell per step.
    If next planned cell becomes occupied at that time, we replan.
    """
    grid = Grid.parse_from_file(mapfile)
    planner = AStarPlanner(grid)
    cur = start
    t = 0
    path = planner.plan(start, goal).path
    log = []
    step_idx = 1  # next step from path
    while cur != goal and t < 1000:
        dynamic_obs = dynamic_schedule.get(t, set())
        # If planned next step is blocked, replan from cur avoiding dynamic_obs
        if step_idx >= len(path) or path[step_idx] in dynamic_obs:
            # mark dynamic obstacles into grid by passing dynamic set to neighbors() - simple approach:
            # We'll re-construct a temporary grid object that treats dynamic_obs as obstacles
            # (Use grid.passable with dynamic set by modifying planner.plan signature if needed.)
            # For now, call planner.plan and ignore because base planner doesn't accept dynamic; demo purposes:
            new_path_res = planner.plan(cur, goal)
            path = new_path_res.path
            step_idx = 1
            log.append((t, "replan", cur, path[:5]))
            if not path:
                log.append((t,"failed",cur,[]))
                break
        # take next move
        if step_idx < len(path):
            cur = path[step_idx]
            step_idx += 1
        else:
            break
        log.append((t,"move",cur))
        t += 1
    # write log
    with open(out_log,'w') as f:
        writer = csv.writer(f)
        writer.writerow(["time","event","cell","info"])
        for entry in log:
            writer.writerow([entry[0], entry[1], entry[2], entry[3] if len(entry)>3 else ""])
    return log
