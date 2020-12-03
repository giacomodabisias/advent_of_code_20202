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
    values = read_input()

if __name__ == "__main__":
    main()