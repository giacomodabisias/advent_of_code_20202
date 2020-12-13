def read_input():
    values = []
    with open("input_two.txt") as f:
        line = f.readline()
        while line:
            values.append(list(line.strip()))
            line = f.readline()
    return values


def get_adj_seats(i, j, seats):
    rows = len(seats)
    cols = len(seats[0])
    adj_seats = []

    # ROWS UP
    original_i = i
    original_j = j
    while i > 0:
        i -= 1
        if seats[i][j] != ".":
            adj_seats.append(seats[i][j])
            break


    # ROWS DOWN
    i = original_i
    j = original_j
    while i < rows - 1:
        i += 1
        if seats[i][j] != ".":
            adj_seats.append(seats[i][j])
            break

    # COLS LEFT
    i = original_i
    j = original_j
    while j > 0:
        j -= 1
        if seats[i][j] != ".":
            adj_seats.append(seats[i][j])
            break

    # COLS RIGHT
    i = original_i
    j = original_j
    while j < cols - 1:
        j += 1
        if seats[i][j] != ".":
            adj_seats.append(seats[i][j])
            break

    # DIAG RIGHT UP
    i = original_i
    j = original_j
    while i > 0 and j < cols - 1:
        i -= 1
        j += 1
        if seats[i][j] != ".":
            adj_seats.append(seats[i][j])
            break

    # DIAG RIGHT DOWN
    i = original_i
    j = original_j
    while i < rows - 1 and j < cols - 1:
        i += 1
        j += 1
        if seats[i][j] != ".":
            adj_seats.append(seats[i][j])
            break

    # DIAG LEFT UP
    i = original_i
    j = original_j
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if seats[i][j] != ".":
            adj_seats.append(seats[i][j])
            break

    # DIAG LEFT DOWN
    i = original_i
    j = original_j
    while i < rows - 1 and j > 0:
        i += 1
        j -= 1
        if seats[i][j] != ".":
            adj_seats.append(seats[i][j])
            break

    return adj_seats


def get_occupied_count(adjs):
    total = 0
    for adj in adjs:
        if adj == "#":
            total += 1
    return total


def mutate(seats):
    mutated = False
    rows = len(seats)
    cols = len(seats[0])

    new_seats = [line.copy() for line in seats]

    for i in range(rows):
        for j in range(cols):
            seat_state = seats[i][j]
            adj_states = get_adj_seats(i, j, seats)
            if seat_state == "L" and "#" not in adj_states:
                mutated = True
                new_seats[i][j] = "#"
            elif seat_state == "#" and get_occupied_count(adj_states) >= 5:
                mutated = True
                new_seats[i][j] = "L"

    return mutated, new_seats


def pretty_print(seats):
    rows = len(seats)
    for i in range(rows):
        print(" ".join(seats[i]))


def main():
    seats = read_input()
    mutated = True

    while mutated:
        mutated, seats = mutate(seats)

    print(get_occupied_count([j for sub in seats for j in sub]))


if __name__ == "__main__":
    main()