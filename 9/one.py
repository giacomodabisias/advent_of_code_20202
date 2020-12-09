def find_double_sum(values, to_find):
    for i in values:
        if to_find - i in values:
            return True
    return False


def read_input():
    values = []
    with open("input_one.txt") as f:
        line = f.readline()
        while line:
            v = int(line.strip())
            values.append(v)
            line = f.readline()
    return values


def is_valid(number, window):
    # This just works since there are no repeated numbers in the window :D
    values = set(window)
    return find_double_sum(values, number)


def main():
    numbers = read_input()
    window_size = 25
    window = numbers[:window_size]
    numbers = numbers[window_size:]

    for number in numbers:
        if not is_valid(number, window):
            print(f"{number} is invalid")
        window = window[1:]
        window.append(number)

if __name__ == "__main__":
    main()