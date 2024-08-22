import functools
import operator
from pathlib import Path

OPERATORS = {
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
}


def load_input() -> dict[str, str]:
    lines = Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines()
    circuit: dict[str, str] = {}
    for line in lines:
        source, _, dest = line.partition(" -> ")
        circuit[dest] = source
    return circuit


def signal_on_a(circuit: dict[str, str]) -> int:
    @functools.cache
    def signal(source: str) -> int:
        tokens = source.split(" ")

        if len(tokens) == 1:
            try:
                return int(tokens[0])
            except ValueError:
                return signal(circuit[tokens[0]])

        if tokens[0] == "NOT":
            return ~signal(tokens[1]) & 65535

        left, gate, right = tokens
        return OPERATORS[gate](signal(left), signal(right))

    return signal(circuit["a"])


def part_1(circuit: dict[str, str]) -> int:
    return signal_on_a(circuit)


def part_2(circuit: dict[str, str]) -> int:
    circuit["b"] = str(part_1(circuit))
    return signal_on_a(circuit)


if __name__ == "__main__":
    circuit = load_input()
    print("Part 1:", part_1(circuit))
    print("Part 2:", part_2(circuit))
