import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Stats:
    velocity: int
    flight: int
    rest: int


@dataclass
class State:
    remaining: int
    distance: int
    points: int
    flying: bool


def load_input() -> dict[str, Stats]:
    pattern = re.compile(
        r"(\w+) can fly (\d+) km/s for (\d+) seconds, "
        r"but then must rest for (\d+) seconds\."
    )
    deer: dict[str, Stats] = {}
    lines = Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines()
    for line in lines:
        if match := pattern.fullmatch(line):
            name, *specs = match.groups()
            deer[name] = Stats(*map(int, specs))
    return deer


def run_race(deer: Mapping[str, Stats]) -> Iterable[State]:
    states = {
        name: State(specs.flight, 0, 0, flying=True) for name, specs in deer.items()
    }
    for _ in range(2503):
        for name, state in states.items():
            if state.flying:
                state.distance += deer[name].velocity
            state.remaining -= 1
            if state.remaining == 0:
                state.remaining = deer[name].rest if state.flying else deer[name].flight
                state.flying = not state.flying
        max_distance = max(state.distance for state in states.values())
        for state in states.values():
            if state.distance == max_distance:
                state.points += 1
    return states.values()


def part_1(deer: Mapping[str, Stats]) -> int:
    return max(state.distance for state in run_race(deer))


def part_2(deer: Mapping[str, Stats]) -> int:
    return max(state.points for state in run_race(deer))


if __name__ == "__main__":
    deer = load_input()
    print("Part 1:", part_1(deer))
    print("Part 2:", part_2(deer))
