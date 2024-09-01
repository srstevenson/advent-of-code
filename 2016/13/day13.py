from collections import deque
from pathlib import Path


def load_input() -> int:
    return int(Path(__file__).parent.joinpath("input.txt").read_text().strip())


def is_open_space(x: int, y: int, favourite: int) -> bool:
    value = x * x + 3 * x + 2 * x * y + y + y * y
    value += favourite
    return value.bit_count() % 2 == 0


def enqueue_neighbours(  # noqa: PLR0913
    favourite: int,
    x: int,
    y: int,
    steps: int,
    seen: set[tuple[int, int]],
    queue: deque[tuple[int, int, int]],
) -> None:
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        xp, yp = x + dx, y + dy
        if (
            xp >= 0
            and yp >= 0
            and (xp, yp) not in seen
            and is_open_space(xp, yp, favourite)
        ):
            seen.add((xp, yp))
            queue.appendleft((xp, yp, steps + 1))


def part_1(favourite: int) -> int:
    queue = deque([(1, 1, 0)])
    seen = {(1, 1)}

    while queue:
        x, y, steps = queue.pop()
        if x == 31 and y == 39:
            return steps
        enqueue_neighbours(favourite, x, y, steps, seen, queue)

    raise RuntimeError("Solution not found")


def part_2(favourite: int) -> int:
    queue = deque([(1, 1, 0)])
    seen = {(1, 1)}

    while queue:
        x, y, steps = queue.pop()
        if steps == 50:
            return len(seen)
        enqueue_neighbours(favourite, x, y, steps, seen, queue)

    raise RuntimeError("Solution not found")


if __name__ == "__main__":
    favourite = load_input()
    print("Part 1:", part_1(favourite))
    print("Part 2:", part_2(favourite))
