import os

def handle_lines(lines: list[str]) -> list:
    input_lines = []
    for line in lines:
        line = line.rstrip("\n")
        line = line.split(" | ")[1]
        line = line.split(" ")
        input_lines.append(line)
    
    return input_lines

def discover_numbers(basic_inputs: list[str]) -> tuple[str]:
    one = 0
    four = 0
    seven = 0
    eight = 0

    for line in basic_inputs:
        for element in line:
            match len(element):
                case 2:
                    one += 1
                case 4:
                    four += 1
                case 3:
                    seven += 1
                case 7:
                    eight += 1
    
    print(one, four, seven, eight)
    return (one, four, seven, eight)




if __name__ == "__main__":

    cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(cwd, "input"), "r") as f:
        lines = f.readlines()

    basic_inputs = handle_lines(lines)

    one, four, seven, eight = discover_numbers(basic_inputs)
    
    result = one + four + seven + eight
    print(result)