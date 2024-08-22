from pathlib import Path


def load_input() -> list[str]:
    return Path(__file__).parent.joinpath("input.txt").read_text().strip().splitlines()


def part_1(ips: list[str]) -> int:
    support_tls = 0
    for ip in ips:
        abba, abba_hs, in_hs = False, False, False
        for i in range(len(ip) - 3):
            if ip[i] in "[]":
                in_hs = not in_hs
            elif ip[i] != ip[i + 1] and ip[i] == ip[i + 3] and ip[i + 1] == ip[i + 2]:
                if in_hs:
                    abba_hs = True
                else:
                    abba = True
        support_tls += abba and not abba_hs
    return support_tls


def part_2(ips: list[str]) -> int:
    support_ssl = 0
    for ip in ips:
        abas, babs, in_hs = set(), set(), False
        for i in range(len(ip) - 2):
            if ip[i] in "[]":
                in_hs = not in_hs
            elif ip[i] != ip[i + 1] and ip[i] == ip[i + 2] and ip[i + 1] not in "[]":
                if in_hs:
                    babs.add(ip[i : i + 3])
                else:
                    abas.add(ip[i : i + 3])
        for aba in abas:
            if aba[1] + aba[0] + aba[1] in babs:
                support_ssl += 1
                break
    return support_ssl


if __name__ == "__main__":
    ips = load_input()
    print("Part 1:", part_1(ips))
    print("Part 2:", part_2(ips))
