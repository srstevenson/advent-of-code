from collections import defaultdict
from collections.abc import Iterable, Mapping
from pathlib import Path


def load_input() -> tuple[str, dict[str, list[str]]]:
    replacements = defaultdict(list)
    lines = Path(__file__).parent.joinpath("input.txt").read_text().splitlines()
    for line in lines:
        left, _, right = line.strip().partition(" => ")
        if right:
            replacements[left].append(right)
        elif left:
            return left, replacements
    raise RuntimeError("Invalid input file")


def part_1(molecule: str, replacements: Mapping[str, Iterable[str]]) -> int:
    molecules = set()
    for source, targets in replacements.items():
        for i in range(len(molecule) - len(source) + 1):
            if molecule[i : i + len(source)] == source:
                for target in targets:
                    molecules.add(molecule[:i] + target + molecule[i + len(source) :])
    return len(molecules)


def part_2(molecule: str, replacements: Mapping[str, Iterable[str]]) -> int:
    contractions = {
        target: source for source, targets in replacements.items() for target in targets
    }
    steps = 0
    while molecule != "e":
        for source, target in contractions.items():
            for i in range(len(molecule) - len(source) + 1):
                if molecule[i : i + len(source)] == source:
                    molecule = molecule[:i] + target + molecule[i + len(source) :]
                    steps += 1
                    break
    return steps


if __name__ == "__main__":
    inputs = load_input()
    print("Part 1:", part_1(*inputs))
    print("Part 2:", part_2(*inputs))
