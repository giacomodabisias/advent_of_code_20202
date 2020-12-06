def read_input():
    answers = []
    with open("input_one.txt", "r") as f:
        lines = f.readlines()
    answer_lines = []
    for line in lines:
        if line == "\n":
            answers.append(answer_lines)
            answer_lines = []
        else:
            line = line.strip()
            answer_lines.append(line)
    answers.append(answer_lines)
    return answers


def main():
    group_answers = read_input()
    total = 0
    for group_answer in group_answers:
        yes_answers = set()
        for person_answers in group_answer:
            for answer in person_answers:
                yes_answers.add(answer)
        total += len(yes_answers)
    print(total)


if __name__ == "__main__":
    main()