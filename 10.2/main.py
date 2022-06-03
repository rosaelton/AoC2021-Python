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
            return 3
        case "]":
            return 57
        case "}":
            return 1197
        case ">":
            return 25137


def count_corruption_points(lines: list[str]) -> int:
    corruption_points = 0
    for line in lines:
        opened_chars = []
        for char in line:
            if char == "<" or char == "{" or char == "[" or char == "(":
                opened_chars.append(char)
            if char == ">" or char == "}" or char == "]" or char == ")":
                if inverted_char(opened_chars[-1]) == char:
                    opened_chars = opened_chars[:-1]
                else:
                    corruption_points += char_points(char)
                    break
    return corruption_points
                

if __name__ == "__main__":

    cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(cwd, "input"), "r") as f:
        lines = f.readlines()

    lines = handle_lines(lines)
    print(count_corruption_points(lines))
