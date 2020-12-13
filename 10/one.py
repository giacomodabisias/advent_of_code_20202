def read_input():
    values = []
    with open("input_one.txt") as f:
        line = f.readline()
        while line:
            v = int(line.strip())
            values.append(v)
            line = f.readline()
    return values


def get_possible_adapters(current_voltage, max_diff, adapters):
    possible_adapters = []
    for adapter in adapters:
        if current_voltage <= adapter <= current_voltage + max_diff:
            possible_adapters.append(adapter)
    return possible_adapters


def get_sequence(current_sequence, remaining_adapters, current_voltage, max_diff):
    possible_adapters = get_possible_adapters(current_voltage, max_diff, remaining_adapters)
    if len(possible_adapters) == 0:
        return
    else:
        for possible_adapter in possible_adapters:
            remaining_adapters.remove(possible_adapter)
            current_sequence.append(possible_adapter)
            get_sequence(current_sequence, remaining_adapters, possible_adapter, max_diff)
            if len(remaining_adapters) == 0:
                return
            current_sequence.remove(possible_adapter)


def main():
    adapters = read_input()
    adapters.append(0)
    adapters.sort()
    outlet_voltage = adapters[-1] + 3
    adapters.append(outlet_voltage)
    voltage = 0
    max_diff = 3
    current_sequence = []
    get_sequence(current_sequence, adapters, voltage, max_diff)

    one_diff = 0
    three_diff = 0
    for idx in range(1, len(current_sequence)):
        if current_sequence[idx] - current_sequence[idx - 1] == 1:
            one_diff +=1
        elif current_sequence[idx] - current_sequence[idx - 1] == 3:
            three_diff += 1
    print(one_diff, three_diff, one_diff*three_diff)


if __name__ == "__main__":
    main()