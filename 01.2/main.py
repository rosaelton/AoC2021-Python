import os

def list_cleaner(raw_radar_list: list) -> list:
    '''
    Clean \n from all the elements of the
    opened list, converting them to int type.
    '''
    cleaned_radar_list = []
    for element in raw_radar_list:
        element = element.replace("\n", "")
        element = int(element)
        cleaned_radar_list.append(element)

    return cleaned_radar_list


def increasing_counter(radar_readings: list) -> int:
    '''
    Counts the number of increases from the respective previous reading
    '''
    previous_reading = None
    increments = 0

    for reading in radar_readings:
        if previous_reading is not None:
            if reading > previous_reading:
                increments += 1

        previous_reading = reading

    return increments


def sum_radar_readings(radar_readings: list) -> list:
    '''
    Creates a list of sums from the original radar readings. Three by three sliding window.
    '''
    list_of_sums = []
    current_summing_list = []

    for reading in radar_readings:
        current_summing_list.append(reading)

        if len(current_summing_list) == 3:
            list_of_sums.append(sum(current_summing_list))
            current_summing_list.pop(0)

    return list_of_sums

def compare_every_third(radar_readings: list) -> int:
    '''
    Since it is only necessary to compare each sum window with its immediate neighbor, there will be always 2 of 3 elements
    which are common to both. The "left" window has the elements a, b, c and the "right" window the elements b, c, d. If d > a
    then sum(a, b, c) > sum(b, c, d) by transitity.

    radar_readings: the original readings from input cleaned.
    '''
    increments = 0

    for index, reading in enumerate(radar_readings):
        left = reading
        try:
            right = radar_readings[index + 3]
        except IndexError:
            break

        if right > left:
            increments += 1
    
    return increments
      

if __name__ == "__main__":
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, "input"), "r") as f:
        opened_list = f.readlines()

    radar_readings = list_cleaner(opened_list)
    sums_of_radar_readings = sum_radar_readings(radar_readings)

    increments = increasing_counter(sums_of_radar_readings)
    print(increments)
    
    alternative_solution = compare_every_third(radar_readings)
    print(alternative_solution)
