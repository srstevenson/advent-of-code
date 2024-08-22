import re
from pathlib import Path

EVIDENCE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def load_input() -> dict[int, dict[str, int]]:
    pattern = re.compile(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)")
    aunts = {}
    lines = Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines()
    for line in lines:
        if m := pattern.fullmatch(line):
            aunts[int(m.group(1))] = {
                m.group(2): int(m.group(3)),
                m.group(4): int(m.group(5)),
                m.group(6): int(m.group(7)),
            }
    return aunts


def part_1(aunts: dict[int, dict[str, int]]) -> int:
    for aunt, compounds in aunts.items():
        if all(compounds[c] == EVIDENCE[c] for c in compounds):
            return aunt
    raise RuntimeError("Solution not found")


def part_2(aunts: dict[int, dict[str, int]]) -> int:
    def matches(compound: str, amount: int) -> bool:
        match compound:
            case "cats" | "trees":
                return amount > EVIDENCE[compound]
            case "pomeranians" | "goldfish":
                return amount < EVIDENCE[compound]
            case _:
                return amount == EVIDENCE[compound]

    for aunt, compounds in aunts.items():
        if all(matches(*compound) for compound in compounds.items()):
            return aunt
    raise RuntimeError("Solution not found")


if __name__ == "__main__":
    aunts = load_input()
    print("Part 1:", part_1(aunts))
    print("Part 2:", part_2(aunts))
