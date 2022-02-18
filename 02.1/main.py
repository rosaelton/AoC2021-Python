import os

def list_cleaner(raw_radar_list: list) -> list:
    '''
    Clean \n from all the elements of the
    opened list, converting them to int type.
    '''
    cleaned_radar_list = []
    for element in raw_radar_list:
        element = element.replace("\n", "")
        element = element.split(" ")
        element[1] = int(element[1])
        element = tuple(element)
        cleaned_radar_list.append(element)

    return cleaned_radar_list


def position_calculator(moves: list) -> int:
    horizontal_location = 0
    depth_location = 0

    for move in moves:
        if move[0] == "forward":
            horizontal_location += move[1]
        elif move[0] == "up":
            depth_location -= move[1]
        else:
            depth_location += move[1]
    
    product = horizontal_location * depth_location
    return product


if __name__ == "__main__":

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, "input"), "r") as f:
        opened_list = f.readlines()

    moves = list_cleaner(opened_list)
    position = position_calculator(moves)
    print(position)
    
