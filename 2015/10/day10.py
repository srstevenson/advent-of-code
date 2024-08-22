from pathlib import Path


def load_input() -> list[int]:
    return list(
        map(int, Path(__file__).parent.joinpath("input.txt").read_text().strip())
    )


def look_and_say(sequence: list[int], iters: int) -> int:
    for _ in range(iters):
        next_sequence: list[int] = []
        last_digit, count = sequence[0], 1
        for digit in sequence[1:]:
            if digit != last_digit:
                next_sequence.extend([count, last_digit])
                last_digit, count = digit, 0
            count += 1
        next_sequence.extend([count, last_digit])
        sequence = next_sequence
    return len(sequence)


def part_1(sequence: list[int]) -> int:
    return look_and_say(sequence, 40)


def part_2(sequence: list[int]) -> int:
    return look_and_say(sequence, 50)


if __name__ == "__main__":
    sequence = load_input()
    print("Part 1:", part_1(sequence))
    print("Part 2:", part_2(sequence))
