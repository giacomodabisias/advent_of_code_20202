from collections import defaultdict


def read_input():
    bags = defaultdict(lambda: [])
    with open("input_one.txt") as f:
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


def search_for_bags(bags, item, total, index, from_bag):
    for bag in bags:
        colour = bag[0]
        if colour == item:
            total.add(from_bag)
            break
        else:
            if colour in index:
                search_for_bags(index[colour], item, total, index, from_bag + "->" + colour)


def main():
    bags = read_input()

    searchable = "shiny gold"
    total = set()
    for k in bags.keys():
        search_for_bags(bags[k], searchable, total, bags, k)
    unique = set()
    for way in total:
        unique.add(way.split("->")[0])
    print(len(unique))


if __name__ == "__main__":
    main()