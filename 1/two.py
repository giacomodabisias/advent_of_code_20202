def find_double_sum(values, to_find):
    for i in values:
        if to_find - i in values:
            return i, to_find - i
    return None, None


def read_input():
    values = set()
    with open("input_two.txt") as f:
        line = f.readline()
        while line:
            v = int(line.strip())
            values.add(v)
            line = f.readline()
    return values


def main():
    to_find = 2020
    values = read_input()

    for k in values:
        values.remove(k)
        i, j = find_double_sum(values, to_find - k)
        if i is not None and j is not None:
            print(i, j, k, i*j*k)
            break
        values.add(k)


if __name__ == "__main__":
    main()