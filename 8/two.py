def read_input():
    instructions = dict()
    counter = 0
    with open("input_two.txt") as f:
        line = f.readline()
        while line:
            values = line.strip().split(" ")
            instructions[counter] = (values[0], int(values[1]))
            counter += 1
            line = f.readline()
    return instructions


def execute(instruction, line, accumulator):
    op = instruction[0]
    value = instruction[1]
    if op == "nop":
        return line + 1, accumulator
    elif op == "acc":
        return line + 1, accumulator + value
    elif op == "jmp":
        return line + value, accumulator


def does_terminate(instructions):
    accumulator = 0
    executed = set()
    line = 0

    while True:
        if line not in executed:
            executed.add(line)
            if line in instructions:
                line, accumulator = execute(instructions[line], line, accumulator)
            else:
                print(f"Terminated on line {line} with acc: {accumulator}")
                return True
        else:
            return False


def switch(instructions, change_line):
    new_instructions = instructions.copy()
    if new_instructions[change_line][0] == "nop":
        new_instructions[change_line] = ("jmp", new_instructions[change_line][1])
    elif instructions[change_line][0] == "jmp":
        new_instructions[change_line] = ("nop", new_instructions[change_line][1])
    else:
        raise RuntimeError(f"Unhandled operation {new_instructions[change_line][0]}")
    return new_instructions


def main():
    original_instructions = read_input()
    all_nop_and_jmp = [idx for idx, operation in original_instructions.items() if (operation[0] == "jmp" or operation[0] == "nop")]
    current_instructions = original_instructions.copy()

    while len(all_nop_and_jmp) > 0:
        if does_terminate(current_instructions):
            break
        current_instructions = switch(original_instructions, all_nop_and_jmp.pop())


if __name__ == "__main__":
    main()