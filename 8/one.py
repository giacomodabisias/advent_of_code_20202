def read_input():
    instructions = dict()
    counter = 0
    with open("input_one.txt") as f:
        line = f.readline()
        while line:
            values = line.strip().split(" ")
            instructions[counter] = (values[0], int(values[1]))
            counter += 1
            line = f.readline()
    return instructions


ACCUMULATOR = 0


def execute(instruction, line):
    global ACCUMULATOR
    op = instruction[0]
    value = instruction[1]
    if op == "nop":
        return line + 1
    elif op == "acc":
        ACCUMULATOR += value
        return line + 1
    elif op == "jmp":
        return line + value


def main():
    instructions = read_input()
    executed = set()
    line = 0

    while True:
        if line not in executed:
            executed.add(line)
            line = execute(instructions[line], line)
        else:
            print(ACCUMULATOR)
            break


if __name__ == "__main__":
    main()