from pathlib import Path


def load_input() -> str:
    return Path(__file__).parent.joinpath("input.txt").read_text()


def part_1(directions: str) -> int:
    return sum(1 if d == "(" else -1 for d in directions)


def part_2(directions: str) -> int:
    floor = 0
    for position, direction in enumerate(directions, start=1):
        floor += 1 if direction == "(" else -1
        if floor == -1:
            return position
    raise RuntimeError("Solution not found")


if __name__ == "__main__":
    directions = load_input()
    print("Part 1:", part_1(directions))
    print("Part 2:", part_2(directions))
