# src/grid.py
from typing import List, Tuple, Dict, Optional
import math

Cell = Tuple[int,int]

class Grid:
    def __init__(self, width: int, height: int, cells: Dict[Cell,int], obstacles: set=None):
        self.width = width
        self.height = height
        self.cells = cells  # dict: (r,c) -> cost (>=1)
        self.obstacles = obstacles if obstacles else set()  # occupied cells
    
    @staticmethod
    def parse_from_file(path: str):
        # File format: first line "W H"
        # Next H lines each contain W integers: cost or -1 for static obstacle.
        cells = {}
        obstacles = set()
        with open(path,'r') as f:
            header = f.readline().strip()
            if not header:
                raise ValueError("Empty map file")
            W,H = map(int, header.split())
            for r in range(H):
                row = f.readline().strip().split()
                if len(row) < W:
                    raise ValueError("row length mismatch")
                for c, token in enumerate(row):
                    v = int(token)
                    if v < 0:
                        obstacles.add((r,c))
                    else:
                        cells[(r,c)] = max(1, v)
        return Grid(W,H,cells,obstacles)
    
    def in_bounds(self, cell: Cell) -> bool:
        r,c = cell
        return 0 <= r < self.height and 0 <= c < self.width
    
    def passable(self, cell: Cell, dynamic_obstacles:set=None) -> bool:
        if cell in self.obstacles:
            return False
        if dynamic_obstacles and cell in dynamic_obstacles:
            return False
        return True
    
    def cost(self, cell: Cell) -> int:
        return self.cells.get(cell, 999999)
    
    def neighbors(self, cell: Cell, dynamic_obstacles:set=None) -> List[Cell]:
        r,c = cell
        candidates = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
        return [n for n in candidates if self.in_bounds(n) and self.passable(n, dynamic_obstacles)]