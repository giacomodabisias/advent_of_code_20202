from collections import defaultdict


def read_input():
    answers = []
    with open("input_two.txt", "r") as f:
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
        yes_answers = defaultdict(lambda: 0)
        for person_answers in group_answer:
            for answer in person_answers:
                yes_answers[answer] += 1
        for k, v in yes_answers.items():
            if v == len(group_answer):
                total += 1
    print(total)


if __name__ == "__main__":
    main()
