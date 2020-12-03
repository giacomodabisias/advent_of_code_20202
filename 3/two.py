from typing import List


def read_input():
    values = []
    with open("input_two.txt") as f:
        line = f.readline()
        while line:
            values.append(line.strip())
            line = f.readline()
    return values


def get_tree_count(right: int, down: int, forest: List[str]) -> int:
    tree_count = 0
    line_length = len(forest[0])
    forest_length = len(forest)
    x = 0
    y = 0
    while y < forest_length - 1:
        x = (x + right) % line_length
        y += down
        if forest[y][x] == "#":
            tree_count += 1

    return tree_count


def main():
    forest = read_input()
    tree_count = 1
    inputs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for i in inputs:
        tree_count *= get_tree_count(right=i[0], down=i[1], forest=forest)
    print(tree_count)


if __name__ == "__main__":
    main()