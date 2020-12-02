def find_double_sum(values, to_find):
    for i in values:
        if to_find - i in values:
            return i, to_find - i


def read_input():
    values = set()
    with open("input_one.txt") as f:
        line = f.readline()
        while line:
            v = int(line.strip())
            values.add(v)
            line = f.readline()
    return values


def main():
    to_find = 2020
    values = read_input()
    i, j = find_double_sum(values, to_find)
    print(i, j, i*j)


if __name__ == "__main__":
    main()