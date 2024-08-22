from collections.abc import Sequence
from pathlib import Path


def load_input() -> list[str]:
    return Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines()


def execute(instructions: Sequence[str], registers: dict[str, int]) -> int:
    i = 0
    while i < len(instructions):
        inst = instructions[i]
        if inst.startswith("cpy"):
            x, y = inst.removeprefix("cpy ").split(" ")
            registers[y] = registers[x] if x.isalpha() else int(x)
            i += 1
        elif inst.startswith("inc"):
            registers[inst.removeprefix("inc ")] += 1
            i += 1
        elif inst.startswith("dec"):
            registers[inst.removeprefix("dec ")] -= 1
            i += 1
        else:
            x, y = inst.removeprefix("jnz ").split(" ")
            x = registers[x] if x.isalpha() else int(x)
            i += 1 if x == 0 else int(y)
    return registers["a"]


def part_1(instructions: Sequence[str]) -> int:
    return execute(instructions, {"a": 0, "b": 0, "c": 0, "d": 0})


def part_2(instructions: Sequence[str]) -> int:
    return execute(instructions, {"a": 0, "b": 0, "c": 1, "d": 0})


if __name__ == "__main__":
    instructions = load_input()
    print("Part 1:", part_1(instructions))
    print("Part 2:", part_2(instructions))
