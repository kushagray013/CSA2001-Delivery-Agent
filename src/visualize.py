# src/visualize.py
import matplotlib.pyplot as plt
from src.grid import Grid

def draw_grid(grid, path=None, dynamic_obs=None, savepath=None):
    H,W = grid.height, grid.width
    img = [[0]*W for _ in range(H)]
    for (r,c),cost in grid.cells.items():
        img[r][c] = cost
    # convert to simple plot: obstacles as black
    plt.figure(figsize=(6,6))
    plt.imshow(img, origin='upper')
    if path:
        ys = [p[0] for p in path]; xs = [p[1] for p in path]
        plt.plot(xs, ys, marker='o')
    if dynamic_obs:
        for (r,c) in dynamic_obs:
            plt.scatter(c, r, marker='s')
    if savepath:
        plt.savefig(savepath)
    else:
        plt.show()
    plt.close()
