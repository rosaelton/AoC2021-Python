import os

def handle_lines(lines: list[str]) -> list:
    lines = lines[0].split(",")
    positions = [int(x) for x in lines]

    minimal_position = min(positions)
    maximal_position = max(positions)

    minimal_fuel = None

    for alignment_position in range(minimal_position, maximal_position + 1):
        total_spent_fuel = 0
        for position in positions:
            crab_spent_fuel = abs(position - alignment_position)
            total_spent_fuel += crab_spent_fuel
        if minimal_fuel is None or total_spent_fuel < minimal_fuel:
            minimal_fuel = total_spent_fuel 
    
    print(minimal_fuel)


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

    crab_positions = handle_lines(lines)