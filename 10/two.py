def read_input():
    values = []
    with open("input_two.txt") as f:
        line = f.readline()
        while line:
            v = int(line.strip())
            values.append(v)
            line = f.readline()
    return values


def get_possible_adapters(current_voltage, adapters):
    possible_adapters = []
    if current_voltage - 1 in adapters:
        possible_adapters.append(current_voltage - 1)
    if current_voltage - 2 in adapters:
        possible_adapters.append(current_voltage - 2)
    if current_voltage - 3 in adapters:
        possible_adapters.append(current_voltage - 3)
    return possible_adapters


def get_sequence_fast(adapters, voltage):
    if voltage == 0:
        return 1
    available = get_possible_adapters(voltage, adapters)
    total = 0
    for adp in available:
        adapters.remove(adp)
        total += get_sequence_fast(adapters, adp)
        adapters.add(adp)
    return total


def main():
    adapters = read_input()
    adapters.sort()
    outlet_voltage = adapters[-1] + 3

    print(get_sequence_fast(set(adapters), outlet_voltage))


if __name__ == "__main__":
    main()
