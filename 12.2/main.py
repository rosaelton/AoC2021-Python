from cgitb import small
import os
import copy

def handle_lines(lines: list[str]) -> list[str]:
    lines = [x.rstrip("\n") for x in lines]
    return lines


def recursive_search(connections: dict[list[str]], current_paths: list[list[str]]):
    current_paths = copy.deepcopy(current_paths)

    if len(current_paths) == 0:
        new_connections = connections["start"]

        for connection in new_connections:
            current_paths.append(["start", connection])

        return current_paths
    
    new_paths = []
    used_routes = set()
    for path in current_paths:
        current_cave = path[-1]

        if current_cave == "end":
            continue

        current_cave_children: list[str] = connections[current_cave]

        for child in current_cave_children:
            if child == "start":
                continue

            if child == "end":
                new_paths.append(path + ["end"])
                used_routes.add(tuple(path))

            if child.isupper():
                new_paths.append(path + [child])
                used_routes.add(tuple(path))

            else:
                can_repeat_small_caves = True
                for cave in path:
                    if cave.islower():
                        revisited_count = path.count(cave)
                        if revisited_count >= 2:
                            can_repeat_small_caves = False
                            break
                
                child_counter = path.count(child)
                if can_repeat_small_caves or child_counter == 0:
                    new_paths.append(path + [child])
                    used_routes.add(tuple(path))

    for used_route in used_routes:
        current_paths.remove(list(used_route))

    current_paths.extend(new_paths)

    return current_paths


def path_finder(lines: list[str]):

    connections: dict[list[str]] = dict()

    for line in lines:
        first, second = line.split("-")

        if first in connections:
            connections[first].append(second)
        else:
            connections[first] = [second]
        if second in connections:
            connections[second].append(first)
        else:
            connections[second] = [first]
    
    del connections["end"]

    paths: list[list] = []


    while True:
        recursive_new_paths = recursive_search(connections, paths)

        if paths == recursive_new_paths:
            break

        paths = recursive_new_paths
    
    unique = []
    for path in paths:
        path = tuple(path)
        if path[-1] == "end" and path not in unique:
            unique.append(path)
    
    print(len(set(unique)))


if __name__ == "__main__":

    cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(cwd, "input"), "r") as f:
        lines = f.readlines()

    lines = handle_lines(lines)
    path_finder(lines)