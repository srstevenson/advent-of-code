from pathlib import Path


def load_input() -> str:
    return Path(__file__).parent.joinpath("input.txt").read_text().strip()


def count_houses(directions: str, *, use_robot: bool = False) -> int:
    x, y = 0, 0
    visited: set[tuple[int, int]] = {(x, y)}
    if use_robot:
        xr, yr = 0, 0
    for d in directions:
        if d == "^":
            y += 1
        elif d == "v":
            y -= 1
        elif d == ">":
            x += 1
        else:
            x -= 1
        visited.add((x, y))
        if use_robot:
            x, y, xr, yr = xr, yr, x, y  # type: ignore[reportPossiblyUnboundVariable]
    return len(visited)


def part_1(directions: str) -> int:
    return count_houses(directions)


def part_2(directions: str) -> int:
    return count_houses(directions, use_robot=True)


if __name__ == "__main__":
    directions = load_input()
    print("Part 1:", part_1(directions))
    print("Part 2:", part_2(directions))
