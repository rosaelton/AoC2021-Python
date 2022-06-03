from contextlib import closing
import os


def handle_lines(lines: list[str]) -> list:
    lines = [x.rstrip("\n") for x in lines]
    return lines


def inverted_char(char: str):
    match char:
        case "(":
            return ")"
        case "[":
            return "]"
        case "{":
            return "}"
        case "<":
            return ">"


def char_points(char: str) -> int:
    match char:
        case ")":
            return 1
        case "]":
            return 2
        case "}":
            return 3
        case ">":
            return 4


def discard_corrupted_lines(lines: list[str]) -> list[str]:
    non_corrupted_lines = []
    for line in lines:
        corrupted_line = False
        opened_chars = []
        for char in line:
            if char == "<" or char == "{" or char == "[" or char == "(":
                opened_chars.append(char)
            if char == ">" or char == "}" or char == "]" or char == ")":
                if inverted_char(opened_chars[-1]) == char:
                    opened_chars = opened_chars[:-1]
                else:
                    corrupted_line = True
                    break
        if not corrupted_line:
            non_corrupted_lines.append(line)
    return non_corrupted_lines


def autocompletion_middle_score(lines: list[str]):

    scores = []

    for line in lines:

        line_completion_score = 0

        opened_chars = []
        for char in line:
            if char == "<" or char == "{" or char == "[" or char == "(":
                opened_chars.append(char)
            if char == ">" or char == "}" or char == "]" or char == ")":
                if inverted_char(opened_chars[-1]) == char:
                    opened_chars = opened_chars[:-1]
        opened_chars = reversed(opened_chars)

        closing_chars = [inverted_char(x) for x in opened_chars]

        for char in closing_chars:
            line_completion_score *= 5
            line_completion_score += char_points(char)
        
        scores.append(line_completion_score)
    
    scores = sorted(scores)
    middle_score = scores[int(len(scores) / 2)]

    return middle_score

        
if __name__ == "__main__":

    cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(cwd, "input"), "r") as f:
        lines = f.readlines()

    lines = handle_lines(lines)
    non_corrupted_lines = discard_corrupted_lines(lines)
    middle_score = autocompletion_middle_score(non_corrupted_lines)
    print(middle_score)
