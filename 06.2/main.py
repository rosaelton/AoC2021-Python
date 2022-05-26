import os

def handle_lines(lines: list[str]) -> list:
    lines = lines[0].split(",")
    lines = [int(x) for x in lines]
    return lines


def simulation(fishes:list, days:int):
    fishes_per_timer = [0] * 9
    for fish in fishes:
        fishes_per_timer[fish] += 1
    
    for _ in range(days):
        first_element = fishes_per_timer[0]
        fishes_per_timer.pop(0)
        fishes_per_timer.append(0)
        fishes_per_timer[8] += first_element
        fishes_per_timer[6] += first_element
    
    return sum(fishes_per_timer)



if __name__ == "__main__":

    cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(cwd, "input"), "r") as f:
        lines = f.readlines()

    fishes = handle_lines(lines)
    print(simulation(fishes, 256))