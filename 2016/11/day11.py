import re
from collections import deque
from collections.abc import Generator
from functools import cache
from itertools import combinations
from pathlib import Path

GENERATOR_PATTERN = re.compile(r"a (\w+) generator")
MICROCHIP_PATTERN = re.compile(r"a (\w+)-compatible microchip")


State = tuple[tuple[str, ...], ...]
CanonicalState = tuple[tuple[int, int], ...]


def load_input() -> State:
    state: list[list[str]] = [[], [], [], []]
    lines = Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines()
    for floor, line in reversed(list(enumerate(lines))):
        for pattern, suffix in [(GENERATOR_PATTERN, "g"), (MICROCHIP_PATTERN, "m")]:
            for element in pattern.findall(line):
                state[floor].append(element[0] + suffix)
    return tuple(map(tuple, state))


@cache
def is_end_state(state: State) -> bool:
    return all(len(state[floor]) == 0 for floor in range(3))


@cache
def is_valid_state(state: State) -> bool:
    for floor in state:
        gens = {item[0] for item in floor if item.endswith("g")}
        if any(item.endswith("m") and item[0] not in gens and gens for item in floor):
            return False
    return True


def generate_next_states(floor: int, state: State) -> Generator[tuple[int, State]]:
    next_floors = (
        [floor - 1, floor + 1] if 0 < floor < 3 else [1] if floor == 0 else [2]
    )
    items_to_move = set(combinations(state[floor], 1)) | set(
        combinations(state[floor], 2)
    )
    for next_floor in next_floors:
        for items in items_to_move:
            new_state = list(map(list, state))
            new_state[next_floor].extend(items)
            new_state[floor] = [item for item in state[floor] if item not in items]
            new_state_tuple = tuple(tuple(sorted(items)) for items in new_state)
            if is_valid_state(new_state_tuple):
                yield next_floor, new_state_tuple


@cache
def canonicalise_state(state: State) -> CanonicalState:
    gens: dict[str, int] = {}
    chips: dict[str, int] = {}
    for floor, items in enumerate(state):
        for item in items:
            if item.endswith("g"):
                gens[item[0]] = floor
            else:
                chips[item[0]] = floor

    return tuple(sorted((gens[element], chips[element]) for element in gens))


def min_steps(state: State) -> int:
    queue: deque[tuple[int, State, int]] = deque([(0, state, 0)])
    visited: set[tuple[int, CanonicalState]] = {(0, canonicalise_state(state))}

    while queue:
        floor, state, steps = queue.pop()

        if is_end_state(state):
            return steps

        for next_floor, next_state in generate_next_states(floor, state):
            canonical_next_state = canonicalise_state(next_state)
            if (next_floor, canonical_next_state) not in visited:
                queue.appendleft((next_floor, next_state, steps + 1))
                visited.add((next_floor, canonical_next_state))

    raise RuntimeError("Solution not found")


def part_1(state: State) -> int:
    return min_steps(state)


def part_2(state: State) -> int:
    mutable_state = list(map(list, state))
    mutable_state[0].extend(["eg", "em", "dg", "dm"])
    return min_steps(tuple(map(tuple, mutable_state)))


if __name__ == "__main__":
    state = load_input()
    print("Part 1:", part_1(state))
    print("Part 2:", part_2(state))
