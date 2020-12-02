from typing import NamedTuple


class Case(NamedTuple):
    minimum: int
    maximum: int
    char: str
    password: str


def read_input():
    values = []
    with open("input_one.txt") as f:
        line = f.readline()
        while line:
            parts = line.split(" ")
            i, j = [int(k) for k in parts[0].split("-")]
            c = parts[1][0]
            p = parts[2]
            line = f.readline()
            values.append(Case(minimum=i,maximum=j,char=c,password=p))
    return values


def is_valid(case: Case):
    occurrences = 0
    char = case.char
    for c in case.password:
        if c == char:
            occurrences += 1

    return case.minimum <= occurrences <= case.maximum


def main():
    values = read_input()
    valid_passwords = 0

    for case in values:
        if is_valid(case):
            valid_passwords += 1

    print(f"Valid passwords: {valid_passwords}")
    print(f"Invalid passwords: {len(values) - valid_passwords}")


if __name__ == "__main__":
    main()