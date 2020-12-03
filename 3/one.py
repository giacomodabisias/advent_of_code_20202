from typing import List


def read_input():
    values = []
    with open("input_one.txt") as f:
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
        y += 1
        if forest[y][x] == "#":
            tree_count += 1

    return tree_count


def main():
    forest = read_input()
    tree_count = get_tree_count(right=3, down=1, forest=forest)
    print(f"Encountered {tree_count} trees")


if __name__ == "__main__":
    main()