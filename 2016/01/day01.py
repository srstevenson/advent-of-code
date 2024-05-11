from pathlib import Path

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def load_input() -> list[str]:
    return Path(__file__).parent.joinpath("input.txt").read_text().strip().split(", ")


def part_1(instructions: list[str]) -> int:
    x, y = 0, 0
    direc = 0

    for inst in instructions:
        turn, blocks = inst[0], int(inst[1:])
        direc = (direc - 1) % 4 if turn == "L" else (direc + 1) % 4
        x += DIRECTIONS[direc][0] * blocks
        y += DIRECTIONS[direc][1] * blocks

    return abs(x) + abs(y)


def part_2(instructions: list[str]) -> int:
    x, y = 0, 0
    direc = 0
    visited = {(x, y)}

    for inst in instructions:
        turn, blocks = inst[0], int(inst[1:])
        direc = (direc - 1) % 4 if turn == "L" else (direc + 1) % 4

        for _ in range(blocks):
            x += DIRECTIONS[direc][0]
            y += DIRECTIONS[direc][1]
            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))

    raise RuntimeError("Solution not found")


if __name__ == "__main__":
    instructions = load_input()
    print("Part 1:", part_1(instructions))
    print("Part 2:", part_2(instructions))
