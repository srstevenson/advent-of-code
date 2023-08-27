import re
from collections.abc import MutableMapping, Sequence
from pathlib import Path


def load_input() -> list[str]:
    return Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


def emulate(registers: MutableMapping[str, int], instructions: Sequence[str]) -> int:
    index = 0
    while index < len(instructions):
        if m := re.fullmatch("hlf (a|b)", instructions[index]):
            registers[m.group(1)] //= 2
            index += 1
        elif m := re.fullmatch("tpl (a|b)", instructions[index]):
            registers[m.group(1)] *= 3
            index += 1
        elif m := re.fullmatch("inc (a|b)", instructions[index]):
            registers[m.group(1)] += 1
            index += 1
        elif m := re.fullmatch(r"jmp ([+-]\d+)", instructions[index]):
            index += int(m.group(1))
        elif m := re.fullmatch(r"jie (a|b), ([+-]\d+)", instructions[index]):
            index += int(m.group(2)) if registers[m.group(1)] % 2 == 0 else 1
        elif m := re.fullmatch(r"jio (a|b), ([+-]\d+)", instructions[index]):
            index += int(m.group(2)) if registers[m.group(1)] == 1 else 1
        else:
            msg = f"Unknown instruction: {instructions[index]}"
            raise ValueError(msg)
    return registers["b"]


def part_1(instructions: Sequence[str]) -> int:
    return emulate({"a": 0, "b": 0}, instructions)


def part_2(instructions: Sequence[str]) -> int:
    return emulate({"a": 1, "b": 0}, instructions)


if __name__ == "__main__":
    instructions = load_input()
    print("Part 1:", part_1(instructions))
    print("Part 2:", part_2(instructions))
