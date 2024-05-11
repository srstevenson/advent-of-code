from pathlib import Path

STEPS = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def load_input() -> list[str]:
    return Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


def part_1(instructions: list[str]) -> str:
    keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    code = ""
    y, x = 1, 1
    for line in instructions:
        for step in line:
            y = min(max(y + STEPS[step][0], 0), 2)
            x = min(max(x + STEPS[step][1], 0), 2)
        code += keypad[y][x]
    return code


def part_2(instructions: list[str]) -> str:
    keypad = [
        [None, None, "1", None, None],
        [None, "2", "3", "4", None],
        ["5", "6", "7", "8", "9"],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None],
    ]
    code = ""
    y, x = 2, 0
    for line in instructions:
        for step in line:
            yp = min(max(y + STEPS[step][0], 0), 4)
            xp = min(max(x + STEPS[step][1], 0), 4)
            if keypad[yp][xp]:
                y, x = yp, xp
        code += keypad[y][x]
    return code


if __name__ == "__main__":
    instructions = load_input()
    print("Part 1:", part_1(instructions))
    print("Part 2:", part_2(instructions))
