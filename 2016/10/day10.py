import re
from collections import defaultdict
from pathlib import Path

VALUE_PATTERN = re.compile(r"value (\d+) goes to bot (\d+)")
GIVES_PATTERN = re.compile(
    r"bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)"
)


def load_input() -> list[str]:
    return Path(__file__).parent.joinpath("input.txt").read_text().splitlines()


def initialise(instructions: list[str]) -> dict[int, set[int]]:
    bots = defaultdict(set)
    for inst in instructions:
        if match := VALUE_PATTERN.fullmatch(inst):
            value, bot = map(int, match.groups())
            bots[bot].add(value)
    return bots


def part_1(instructions: list[str]) -> int:
    bots = initialise(instructions)
    done = set()

    while True:
        for inst in instructions:
            if match := GIVES_PATTERN.fullmatch(inst):
                bot = int(match.group(1))
                if bot not in done and len(bots[bot]) == 2:
                    if bots[bot] == {17, 61}:
                        return bot
                    for type_idx, index_idx, ext_fn in [(2, 3, min), (4, 5, max)]:
                        dest, index = match.group(type_idx), int(match.group(index_idx))
                        value = ext_fn(bots[bot])
                        if dest == "bot":
                            bots[index].add(value)
                        bots[bot].remove(value)
                    done.add(bot)


def part_2(instructions: list[str]) -> None:
    bots = initialise(instructions)
    outputs, done = {}, set()

    while not {0, 1, 2}.issubset(outputs):
        for inst in instructions:
            if match := GIVES_PATTERN.fullmatch(inst):
                bot = int(match.group(1))
                if bot not in done and len(bots[bot]) == 2:
                    for type_idx, index_idx, ext_fn in [(2, 3, min), (4, 5, max)]:
                        dest, index = match.group(type_idx), int(match.group(index_idx))
                        value = ext_fn(bots[bot])
                        if dest == "bot":
                            bots[index].add(value)
                        else:
                            outputs[index] = value
                        bots[bot].remove(value)
                    done.add(bot)

    return outputs[0] * outputs[1] * outputs[2]


if __name__ == "__main__":
    instructions = load_input()
    print("Part 1:", part_1(instructions))
    print("Part 2:", part_2(instructions))
