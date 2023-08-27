import re
from collections.abc import Callable, Iterable
from enum import Enum
from itertools import chain
from operator import not_
from pathlib import Path
from typing import NamedTuple, TypeVar

T = TypeVar("T", bool, int)


class Action(Enum):
    TURN_ON = "turn on"
    TURN_OFF = "turn off"
    TOGGLE = "toggle"


class Instruction(NamedTuple):
    action: Action
    x_min: int
    y_min: int
    x_max: int
    y_max: int


def load_input() -> list[Instruction]:
    pattern = re.compile(r"([a-z ]*) (\d+),(\d+) through (\d+),(\d+)")
    instructions = []
    lines = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
    for line in lines:
        if match := pattern.fullmatch(line):
            action, *coords = match.groups()
            instructions.append(Instruction(Action(action), *map(int, coords)))
    return instructions


def evaluate(
    instructions: Iterable[Instruction],
    *,
    default: T,
    turn_on: Callable[[T], T],
    turn_off: Callable[[T], T],
    toggle: Callable[[T], T],
) -> int:
    grid = [[default for _ in range(1000)] for _ in range(1000)]
    for inst in instructions:
        for y in range(inst.y_min, inst.y_max + 1):
            for x in range(inst.x_min, inst.x_max + 1):
                if inst.action == Action.TURN_ON:
                    grid[y][x] = turn_on(grid[y][x])
                elif inst.action == Action.TURN_OFF:
                    grid[y][x] = turn_off(grid[y][x])
                else:
                    grid[y][x] = toggle(grid[y][x])
    return sum(chain.from_iterable(grid))


def part_1(instructions: Iterable[Instruction]) -> int:
    return evaluate(
        instructions,
        default=False,
        turn_on=lambda _: True,
        turn_off=lambda _: False,
        toggle=not_,
    )


def part_2(instructions: Iterable[Instruction]) -> int:
    return evaluate(
        instructions,
        default=0,
        turn_on=lambda val: val + 1,
        turn_off=lambda val: max(0, val - 1),
        toggle=lambda val: val + 2,
    )


if __name__ == "__main__":
    instructions = load_input()
    print("Part 1:", part_1(instructions))
    print("Part 2:", part_2(instructions))
