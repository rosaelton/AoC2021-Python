from enum import unique
import os

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    

class Folding:

    def __init__(self, axis, value):
        self.axis = axis
        self.value = value

    def __repr__(self):
        return f"Folding(axis={self.axis}, value={self.value})"

class TransparentPaper:

    def __init__(self, points, foldings):

        self.points: list[Point] = points
        self.foldings: list[Folding] = foldings
    
    def __repr__(self):
        return f"TransparentPaper(points={self.points}, foldings={self.foldings})"
    
    def eliminate_duplicates(self):
        unique_points = []
        for point in self.points:
            if point not in unique_points:
                unique_points.append(point)
        self.points = unique_points

    def fold(self):
        for folding in self.foldings:
            if folding.axis == "x":
                for index, point in enumerate(self.points):
                    if point.x > folding.value:
                        new_x_value = folding.value - (point.x - folding.value)
                        self.points[index] = Point(new_x_value, point.y)
            if folding.axis == "y":
                for index, point in enumerate(self.points):
                    if point.y > folding.value:
                        new_y_value = folding.value - (point.y - folding.value)
                        self.points[index] = Point(point.x, new_y_value)

            self.eliminate_duplicates()

    
    def _get_max_coordinates(self):
        max_x = 0
        max_y = 0
        for point in self.points:
            if point.x > max_x:
                max_x = point.x
            if point.y > max_y:
                max_y = point.y

        if max_x == 0 and max_y == 0:
            return None, None
        return max_x, max_y

    def draw_paper(self):
        max_x, max_y = self._get_max_coordinates()
        for y in range(max_y + 1):
            line = ""
            for x in range(max_x + 1):
                if Point(x, y) in self.points:
                    line += "#"
                else:
                    line += "."
            print(line)


def handle_lines(lines: list[str]) -> list[str]:
    lines = lines.split("\n\n")
    points = lines[0].split("\n")
    points = [tuple(x.split(",")) for x in points]
    points = [((int(x[0]), int(x[1]))) for x in points]

    foldings = lines[1].split("\n")
    foldings = [x.lstrip('fold along ') for x in foldings]
    foldings = [tuple(x.split("=")) for x in foldings]
    
    points = [Point(x[0], x[1]) for x in points]
    foldings = [Folding(x[0], int(x[1])) for x in foldings]

    return TransparentPaper(points, foldings)


if __name__ == "__main__":

    cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(cwd, "input"), "r") as f:
        lines = f.read()

    transparent_paper = handle_lines(lines)
    transparent_paper.fold()
    transparent_paper.draw_paper()
