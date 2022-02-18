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

if __name__ == "__main__":
    with open("input") as f:
        opened_list = f.readlines()
    
    radar_readings = list_cleaner(opened_list)

    increments = increasing_counter(radar_readings)
    print(increments)
    
