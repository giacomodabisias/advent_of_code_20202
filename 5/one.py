import math

def read_input():
    rows = []
    with open("input_one.txt") as f:
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


def main():
    boarding_passes = read_input()

    total_rows = 127
    total_cols = 8
    max_seat_id = 0

    for boarding_pass in boarding_passes:
        cols = boarding_pass[:7]
        rows = boarding_pass[7:]
        i, j = parse_pass(cols, rows, total_rows, total_cols)
        max_seat_id = max(max_seat_id, i*8 + j)

    print(max_seat_id)


if __name__ == "__main__":
    main()