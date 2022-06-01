import os
from collections import namedtuple

HeightPoint = namedtuple("HeightPoint", "height row column")

def handle_lines(lines: list[str]) -> list:
    lines = [x.rstrip("\n") for x in lines]
    
    height_map = []
    for line in lines:
        integer_line = []
        for digit in line:
            integer_line.append(int(digit))
        height_map.append(integer_line)

    return height_map


def find_low_points(height_map: list[list[int]]) -> list[int]:

    low_points = []
    for row_index, row in enumerate(height_map):
        for column_index, number in enumerate(row):
            up_neighbor_indexes = (row_index - 1, column_index)
            left_neighbor_indexes = (row_index, column_index - 1)
            right_neighbor_indexes = (row_index, column_index + 1)
            low_neighbor_indexes = (row_index + 1, column_index)

            try:
                if up_neighbor_indexes[0] >= 0 and up_neighbor_indexes[1] >= 0:
                    up_neighbor = height_map[up_neighbor_indexes[0]][up_neighbor_indexes[1]]
                else:
                    up_neighbor = 10
            except IndexError:
                up_neighbor = 10
            
            try:
                if left_neighbor_indexes[0] >= 0 and left_neighbor_indexes[1] >= 0:
                    left_neighbor = height_map[left_neighbor_indexes[0]][left_neighbor_indexes[1]]
                else:
                    left_neighbor = 10
            except IndexError:
                left_neighbor = 10

            try:
                if right_neighbor_indexes[0] >= 0 and right_neighbor_indexes[1] >= 0:
                    right_neighbor = height_map[right_neighbor_indexes[0]][right_neighbor_indexes[1]]
                else:
                    right_neighbor = 10
            except IndexError:
                right_neighbor = 10

            
            try:
                if low_neighbor_indexes[0] >= 0 and low_neighbor_indexes[1] >= 0:
                    low_neighbor = height_map[low_neighbor_indexes[0]][low_neighbor_indexes[1]]
                else:
                    low_neighbor = 10
            except IndexError:
                low_neighbor = 10
            
            if number < up_neighbor and number < left_neighbor and number < right_neighbor and number < low_neighbor:
                low_point = HeightPoint(number, row_index, column_index)
                low_points.append(low_point)
    
    return low_points


def find_basins(height_map: list[list[int]], low_points: list[tuple[int]]) -> list[int]:
    
    basins = []

    for low_point in low_points:
        basin = [low_point]

        point_found_in_cycle = True

        while point_found_in_cycle:
            
            point_found_in_cycle = False

            for basin_point in basin:

                row_index = basin_point.row
                column_index = basin_point.column

                up_neighbor_indexes = (row_index - 1, column_index)
                left_neighbor_indexes = (row_index, column_index - 1)
                right_neighbor_indexes = (row_index, column_index + 1)
                low_neighbor_indexes = (row_index + 1, column_index)

                if up_neighbor_indexes[0] >= 0 and up_neighbor_indexes[1] >= 0:
                    try:
                        up_neighbor = (height_map[up_neighbor_indexes[0]][up_neighbor_indexes[1]], up_neighbor_indexes[0], up_neighbor_indexes[1])
                    except IndexError:
                        up_neighbor = (9, up_neighbor_indexes[0], up_neighbor_indexes[1])
                else:
                    up_neighbor = (9, up_neighbor_indexes[0], up_neighbor_indexes[1])

                if left_neighbor_indexes[0] >= 0 and left_neighbor_indexes[1] >= 0:
                    try:
                        left_neighbor = (height_map[left_neighbor_indexes[0]][left_neighbor_indexes[1]], left_neighbor_indexes[0], left_neighbor_indexes[1])
                    except IndexError:
                        left_neighbor = (9, left_neighbor_indexes[0], left_neighbor_indexes[1])
                else:
                    left_neighbor = (9, left_neighbor_indexes[0], left_neighbor_indexes[1])

                if right_neighbor_indexes[0] >= 0 and right_neighbor_indexes[1] >= 0:
                    try:
                        right_neighbor = (height_map[right_neighbor_indexes[0]][right_neighbor_indexes[1]], right_neighbor_indexes[0], right_neighbor_indexes[1])
                    except IndexError:
                        right_neighbor = (9, right_neighbor_indexes[0], right_neighbor_indexes[1])
                else:
                    right_neighbor = (9, right_neighbor_indexes[0], right_neighbor_indexes[1])

                if low_neighbor_indexes[0] >= 0 and low_neighbor_indexes[1] >= 0:
                    try:
                        low_neighbor = (height_map[low_neighbor_indexes[0]][low_neighbor_indexes[1]], low_neighbor_indexes[0], low_neighbor_indexes[1])
                    except IndexError:
                        low_neighbor = (9, low_neighbor_indexes[0], low_neighbor_indexes[1])
                else:
                    low_neighbor = (9, low_neighbor_indexes[0], low_neighbor_indexes[1])


                if up_neighbor[0] != 9 and up_neighbor not in basin:
                    up_neighbor = HeightPoint(up_neighbor[0], up_neighbor[1], up_neighbor[2])
                    basin.append(up_neighbor)
                    point_found_in_cycle = True
                if left_neighbor[0] != 9 and left_neighbor not in basin:
                    left_neighbor = HeightPoint(left_neighbor[0], left_neighbor[1], left_neighbor[2])
                    basin.append(left_neighbor)
                    point_found_in_cycle = True
                if right_neighbor[0] != 9 and right_neighbor not in basin:
                    right_neighbor = HeightPoint(right_neighbor[0], right_neighbor[1], right_neighbor[2])
                    basin.append(right_neighbor)
                    point_found_in_cycle = True
                if low_neighbor[0] != 9 and low_neighbor not in basin:
                    low_neighbor = HeightPoint(low_neighbor[0], low_neighbor[1], low_neighbor[2])
                    basin.append(low_neighbor)
                    point_found_in_cycle = True
        
        basins.append(basin)
    
    return basins

                 
def find_three_larger_basins(basins: list[list[HeightPoint]]):
    basin_biggest_three = [0, 0, 0]
    for basin in basins:
        smallest_of_biggest_three = min(basin_biggest_three)
        size = len(basin)

        if size > smallest_of_biggest_three:
            basin_biggest_three.append(size)
            basin_biggest_three.remove(smallest_of_biggest_three)
    
    result = 1
    for size in basin_biggest_three:
        result *= size
    
    print(result)

                




if __name__ == "__main__":

    cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(cwd, "input"), "r") as f:
        lines = f.readlines()

    height_map = handle_lines(lines)

    low_points = find_low_points(height_map)
    
    basins = find_basins(height_map, low_points)
    
    find_three_larger_basins(basins)
