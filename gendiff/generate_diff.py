import json


def generate_diff(file_path1, file_path2):
    first_file = get_date_from_file(file_path1)
    second_file = get_date_from_file(file_path2)
    print(first_file)
    print(second_file)


def get_date_from_file(file_path):
    return json.load(open(file_path))



