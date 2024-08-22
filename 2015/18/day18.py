from collections import defaultdict
from itertools import product
from pathlib import Path

Grid = defaultdict[tuple[int, int], bool]

CORNERS = {(0, 0), (0, 99), (99, 0), (99, 99)}
NEIGHBOURS = [xy for xy in product([-1, 0, 1], repeat=2) if xy != (0, 0)]


def load_input() -> Grid:
    grid: Grid = defaultdict(bool)
    lines = Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines()
    for y, row in enumerate(lines):
        for x, light in enumerate(row):
            grid[(x, y)] = light == "#"
    return grid


def evolve_grid(grid: Grid, *, corners_stuck_on: bool = False) -> int:
    for _ in range(100):
        next_grid = grid.copy()
        for x, y in product(range(100), repeat=2):
            if corners_stuck_on and (x, y) in CORNERS:
                continue
            neighbours_on = sum(grid[(x + dx, y + dy)] for dx, dy in NEIGHBOURS)
            if grid[(x, y)] and neighbours_on not in {2, 3}:
                next_grid[(x, y)] = False
            elif not grid[(x, y)] and neighbours_on == 3:
                next_grid[(x, y)] = True
        grid = next_grid
    return sum(grid.values())


def part_1(grid: Grid) -> int:
    return evolve_grid(grid)


def part_2(grid: Grid) -> int:
    for xy in CORNERS:
        grid[xy] = True
    return evolve_grid(grid, corners_stuck_on=True)


if __name__ == "__main__":
    grid = load_input()
    print("Part 1:", part_1(grid))
    print("Part 2:", part_2(grid))
