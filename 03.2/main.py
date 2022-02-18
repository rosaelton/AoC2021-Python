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
 

def oxygen_support(binary_readings: list) -> int:
    binary_readings = binary_readings.copy()
    for i in range(len(binary_readings[0])):
        zero_counter = 0
        one_counter = 0
        for binary in binary_readings:
            if binary[i] == "0":
                zero_counter += 1
            else:
                one_counter += 1

        if zero_counter > one_counter:
            for binary in binary_readings.copy():
                if binary[i] != "0":
                    binary_readings.remove(binary)
        else:
            for binary in binary_readings.copy():
                if binary[i] != "1":
                    binary_readings.remove(binary)

        if len(binary_readings) == 1:
            oxygen = binary_readings[0]
            oxygen = int(oxygen, 2)
            return oxygen


def co2_support(binary_readings: list) -> int:
    for i in range(len(binary_readings[0])):
        zero_counter = 0
        one_counter = 0
        for binary in binary_readings:
            if binary[i] == "0":
                zero_counter += 1
            else:
                one_counter += 1

        if zero_counter <= one_counter:
            for binary in binary_readings.copy():
                if binary[i] != "0":
                    binary_readings.remove(binary)
        else:
            for binary in binary_readings.copy():
                if binary[i] != "1":
                    binary_readings.remove(binary)

        if len(binary_readings) == 1:
            co2 = binary_readings[0]
            co2 = int(co2, 2)
            return co2
            

if __name__ == "__main__":

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, "input"), "r") as f:
        opened_list = f.readlines()

    binaries = list_cleaner(opened_list)

    print(len(binaries))
    oxygen = oxygen_support(binaries)
    
    print(len(binaries))
    co2 = co2_support(binaries)

    support = oxygen * co2
    print(support)
