import os

from sklearn import neighbors

def handle_lines(lines: list[str]) -> list:
    lines = [x.rstrip("\n") for x in lines]
    new_lines = []
    for line in lines:
        new_line = []
        for char in line:
            new_line.append(int(char))
        new_lines.append(new_line)
    return new_lines


def sum_1(fish_lines: list[list[int]]):
    for i, line in enumerate(fish_lines):
        for j, _ in enumerate(line):
            fish_lines[i][j] += 1
    return fish_lines


def check_for_flash(fish_lines: list[list[int]]):
    flashing_fishes = []
    for i, line in enumerate(fish_lines):
        for j, fish in enumerate(line):
            if fish == 10:
                flashing_fishes.append((i, j))
    return flashing_fishes


def find_fish_neighbors(flashing_fishes: list[tuple[int]], all_fishes: list[list[int]]):
    lines = len(all_fishes)
    columns = len(all_fishes[0])

    neighbors_indexes = []
    for flashing_fish in flashing_fishes:
        i = flashing_fish[0]
        j = flashing_fish[1]
        fish_neighbors = [
            (i - 1, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j),
            (i, j + 1),
            (i + 1, j - 1),
            (i + 1, j),
            (i + 1, j + 1)
        ]
        for fish_neighbor in fish_neighbors:
            if fish_neighbor[0] < 0 or fish_neighbor[0] > lines - 1:
                continue
            if fish_neighbor[1] < 0 or fish_neighbor[1] > columns - 1:
                continue
            neighbors_indexes.append(fish_neighbor)
    return neighbors_indexes


def reset_flashed_fishes(fish_lines: list[list[int]]):
    for i, line in enumerate(fish_lines):
        for j, fish in enumerate(line):
            if fish >= 10:
                fish_lines[i][j] = 0
    return fish_lines

        
def updater(fish_lines: list[list[int]], cycles: int):
    flashes = 0
    for _ in range(cycles):
        fish_lines = sum_1(fish_lines)

        flashing = check_for_flash(fish_lines)

        while len(flashing) > 0:
            flashes += len(flashing)

            neighbors = find_fish_neighbors(flashing, fish_lines)
            for neighbor in neighbors:
                fish_lines[neighbor[0]][neighbor[1]] += 1
                flashing = check_for_flash(flashing)
        
        fish_lines = reset_flashed_fishes(fish_lines)
    print(flashes)





        


        
if __name__ == "__main__":

    cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(cwd, "input"), "r") as f:
        lines = f.readlines()

    lines = handle_lines(lines)
    updater(lines, 100)