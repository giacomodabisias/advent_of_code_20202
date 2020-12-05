import math
import itertools


def read_input():
    rows = []
    with open("input_two.txt") as f:
        line = f.readline()
        while line:
            row = line.strip()
            rows.append(row)
            line = f.readline()
    return rows


def parse_pass(cols, rows, total_rows, total_cols):
    f = 0
    b = total_rows
    for col in cols:
        if col == "B":
            f += math.ceil(abs(f - b) / 2)
        elif col == "F":
            b -= math.floor(abs(f - b) / 2)
        else:
            raise RuntimeError("Unexpected column value")

    l = 0
    r = total_cols
    for row in rows:
        if row == "L":
            r -= math.floor(abs(r - l) / 2)
        elif row == "R":
            l += math.ceil(abs(r - l) / 2)
        else:
            raise RuntimeError("Unexpected column value")

    return f, l


def get_id(i, j):
    return (i * 8) + j


def main():
    boarding_passes = read_input()

    total_rows = 127
    total_cols = 8

    boarding_ids = set()
    for boarding_pass in boarding_passes:
        cols = boarding_pass[:7]
        rows = boarding_pass[7:]
        i, j = parse_pass(cols, rows, total_rows, total_cols)
        boarding_ids.add(get_id(i, j))

    min_valid_seat = math.ceil((min(boarding_ids)-(total_cols - 1))/total_cols + 1)
    max_valid_seat = (max(boarding_ids)-(total_cols - 1)) // total_cols

    valid_seats = [
        get_id(i, j) for i, j in (
            itertools.product(
                range(min_valid_seat, max_valid_seat),
                range(0, total_cols)
            )
        )
    ]

    print(set(valid_seats) - boarding_ids)


if __name__ == "__main__":
    main()