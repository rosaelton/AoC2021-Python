import os

def list_cleaner(raw_radar_list: list) -> list:
    '''
    Clean \n from all the elements of the
    opened list, converting them to int type.
    '''
    cleaned_radar_list = []
    for element in raw_radar_list:
        element = element.replace("\n", "")
        cleaned_radar_list.append(element)

    return cleaned_radar_list


def power_consumption(binaries: list) -> int:
    gamma_string = ""
    epsilon_string = ""

    for i in range(len(binaries[0])):
        zero_counter = 0
        one_counter = 0
        for binary in binaries:
            if binary[i] == "0":
                zero_counter += 1
            else:
                one_counter += 1
        if zero_counter > one_counter:
            gamma_string += "0"
            epsilon_string += "1"
        else:
            gamma_string += "1"
            epsilon_string += "0"
    
    # Convert binary strings to ints
    gamma = int(gamma_string, 2)
    epsilon = int(epsilon_string, 2)

    consumption = gamma * epsilon
    return consumption


    


if __name__ == "__main__":

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, "input"), "r") as f:
        opened_list = f.readlines()

    binaries = list_cleaner(opened_list)

    consumption = power_consumption(binaries)
    print(consumption)
