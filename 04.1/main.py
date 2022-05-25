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