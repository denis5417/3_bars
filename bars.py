import json
import sys
from geopy.distance import vincenty


def load_data(filepath):
    try:
        with open(filepath) as file_handler:
            return json.load(file_handler)
    except json.decoder.JSONDecodeError:
        print("В файле не JSON")
    except FileNotFoundError:
        print("Файл не найден")


def get_biggest_bar(bar_data):
    return max(bar_data, key=lambda bar: bar['Cells']['SeatsCount'])['Cells']['Name']


def get_smallest_bar(bar_data):
    return min(bar_data, key=lambda bar: bar['Cells']['SeatsCount'])['Cells']['Name']


def get_closest_bar(bar_data, longitude, latitude):
    find_distance = lambda bar: vincenty(bar["Cells"]['geoData']['coordinates'], [longitude, latitude]).km
    return min(bar_data, key=find_distance)['Cells']['Name']


if __name__ == '__main__':
    if len(sys.argv) > 3:
        filepath = sys.argv[1]
        longitude = sys.argv[2]
        latitude = sys.argv[3]
        bar_data = load_data(filepath)
        print("Самый большой бар – {}".format(get_biggest_bar(bar_data)))
        print("Самый маленький бар - {}".format(get_smallest_bar(bar_data)))
        print("Самый близкий бар – {}".format(get_closest_bar(bar_data, longitude, latitude)))
    else:
        print("Введите путь до файла, и координаты")
