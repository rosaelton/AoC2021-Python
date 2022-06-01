import os
from turtle import right
import numpy as np

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
                up_neighbor = height_map[up_neighbor_indexes[0]][up_neighbor_indexes[1]]
            except IndexError:
                up_neighbor = 10
            
            try:
                left_neighbor = height_map[left_neighbor_indexes[0]][left_neighbor_indexes[1]]
            except IndexError:
                left_neighbor = 10

            try:
                right_neighbor = height_map[right_neighbor_indexes[0]][right_neighbor_indexes[1]]
            except IndexError:
                right_neighbor = 10

            try:
                low_neighbor = height_map[low_neighbor_indexes[0]][low_neighbor_indexes[1]]
            except IndexError:
                low_neighbor = 10
            
            if number < up_neighbor and number < left_neighbor and number < right_neighbor and number < low_neighbor:
                low_points.append(number)
    
    return low_points


def risk_level_sum(low_points: list[str]) -> int:
    risk_level = sum(low_points) + len(low_points)
    return risk_level


if __name__ == "__main__":

    cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(cwd, "input"), "r") as f:
        lines = f.readlines()

    height_map = handle_lines(lines)

    low_points = find_low_points(height_map)
    
    print(risk_level_sum(low_points))