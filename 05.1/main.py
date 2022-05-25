import os

def handle_lines(lines: list[str]) -> list:
    vents = []
    for line in lines:
        line = line.rstrip("\n")
        line = line.replace(" -> ", ",")
        line = line.split(",")
        line = [int(x) for x in line]
        origin = (line[0], line[1])
        end = (line[2], line[3])

        vent = (origin, end)

        vents.append(vent)
  
    return vents

def vents_paths(vents: list[tuple[tuple[int]]]):
    points = []
    for vent in vents:
        line = None

        # Check if it is a point
        if vent[0] == vent[1]:
            line = vent[0]

        # Check for horizontal line
        elif vent[0][1] == vent[1][1]:
            if vent[0][0] < vent[1][0]:
                step = 1
            else:
                step = -1
            line = [(x, vent[0][1]) for x in range(vent[0][0], vent[1][0] + step, step)]

        # Check for vertical line
        elif vent[0][0] == vent[1][0]:
            if vent[0][1] < vent[1][1]:
                step = 1
            else:
                step = -1
            line = [(vent[0][0], y) for y in range(vent[0][1], vent[1][1] + step, step)]
        
        # Diagonal line
        else:
            if vent[0][0] < vent[1][0]:
                horizontal_step = 1
            else:
                horizontal_step = -1
            if vent[0][1] < vent[1][1]:
                vertical_step = 1
            else:
                vertical_step = -1
            line = [(x, y) for x, y in zip(range(vent[0][0], vent[1][0] + horizontal_step, horizontal_step), range(vent[0][1], vent[1][1] + vertical_step, vertical_step))]
        
        for point in line:
            points.append(point)
    
    # This solution with sets is considerably faster.
    duplicated_points = set()
    checked_points = set()
    for point in points:
        if point not in checked_points:
            checked_points.add(point)
        else:
            duplicated_points.add(point)
    
    print(len(duplicated_points))

if __name__ == "__main__":

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, "input"), "r") as f:
        lines = f.readlines()

    processed_input = handle_lines(lines)
    vents_paths(processed_input)