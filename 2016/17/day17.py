import hashlib
from collections import deque
from collections.abc import Generator
from pathlib import Path


def load_input() -> str:
    return Path(__file__).parent.joinpath("input.txt").read_text().strip()


def traverse(passcode: str) -> Generator[str]:
    queue = deque([(0, 0, "")])

    while queue:
        x, y, path = queue.pop()
        if x == 3 and y == 3:
            yield path
            continue
        digest = hashlib.md5(f"{passcode}{path}".encode()).hexdigest()
        for i, (d, dx, dy) in enumerate(
            [("U", 0, -1), ("D", 0, 1), ("L", -1, 0), ("R", 1, 0)]
        ):
            if digest[i] in "bcdef" and 0 <= x + dx < 4 and 0 <= y + dy < 4:
                queue.appendleft((x + dx, y + dy, path + d))


def part_1(passcode: str) -> str:
    return next(traverse(passcode))


def part_2(passcode: str) -> int:
    return max(map(len, traverse(passcode)))


if __name__ == "__main__":
    passcode = load_input()
    print("Part 1:", part_1(passcode))
    print("Part 2:", part_2(passcode))
