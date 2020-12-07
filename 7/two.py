from collections import defaultdict


def read_input():
    bags = defaultdict(lambda: [])
    with open("input_two.txt") as f:
        line = f.readline()
        while line:
            parts = line.strip().rstrip(".").split(" bags contain ")
            colour = parts[0]
            if parts[1] != "no other bags":
                for raw_bag in parts[1].split(","):
                    raw_bag = raw_bag.replace("bags", "").replace("bag", "")
                    elements = raw_bag.lstrip(" ").split(" ")
                    quantity = int(elements[0])
                    c = " ".join(elements[1:]).rstrip(" ")
                    bags[colour].append((c, quantity))
            line = f.readline()
    return bags


def search_for_bags(bags, item, total, index, multiplier):
    for bag in bags:
        colour = bag[0]
        new_multiplier = multiplier * bag[1]
        total.append(new_multiplier)
        if colour in index:
            search_for_bags(index[colour], item, total, index, new_multiplier)


def main():
    bags = read_input()

    searchable = "shiny gold"
    total = []
    search_for_bags(bags["shiny gold"], searchable, total, bags, 1)
    print(sum(total))


if __name__ == "__main__":
    main()