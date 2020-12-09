def read_input():
    values = []
    with open("input_two.txt") as f:
        line = f.readline()
        while line:
            v = int(line.strip())
            values.append(v)
            line = f.readline()
    return values


def main():
    numbers = read_input()
    invalid_num = 25918798

    for window in range(2, len(numbers)):
        for i in range(len(numbers) - window):
            window_sum = numbers[i:i+window]
            if sum(window_sum) == invalid_num:
                window_sum.sort()
                print(window_sum[0] + window_sum[-1])
                exit()


if __name__ == "__main__":
    main()