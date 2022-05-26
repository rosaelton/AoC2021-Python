import os

def handle_lines(lines: list[str]) -> list:
    lines = lines[0].split(",")
    lines = [int(x) for x in lines]
    return lines


def simulation(fishes: list, days: int):
    for _ in range(days):
        zero_counter = 0
        zero_indexes = []
        for index, fish in enumerate(fishes):
            if fish == 0:
                zero_counter += 1
                zero_indexes.append(index)
        for _ in range(zero_counter):
            fishes.append(9)
        for i in zero_indexes:
            fishes[i] = 7
        fishes = [(f - 1) for f in fishes]
    print(len(fishes))


if __name__ == "__main__":

    cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(cwd, "input"), "r") as f:
        lines = f.readlines()

    fishes = handle_lines(lines)
    simulation(fishes, 80)