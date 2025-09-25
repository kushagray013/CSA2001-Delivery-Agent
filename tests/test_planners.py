from src.grid import Grid
from src.astar import AStarPlanner
from src.bfs import BFSPlanner
from src.ucs import UCSPlanner

def test_astar_small():
    g = Grid.parse_from_file("maps/map_small.txt")
    planner = AStarPlanner(g)
    res = planner.plan((0,0),(4,6))
    assert res.cost < float("inf")

def test_bfs_small():
    g = Grid.parse_from_file("maps/map_small.txt")
    planner = BFSPlanner(g)
    res = planner.plan((0,0),(4,6))
    assert res.cost < float("inf")

def test_ucs_small():
    g = Grid.parse_from_file("maps/map_small.txt")
    planner = UCSPlanner(g)
    res = planner.plan((0,0),(4,6))
    assert res.cost < float("inf")
