from gendiff.parser import get_date_from_file


def generate_diff(file_path1, file_path2):
    first_file = get_date_from_file(file_path1)
    second_file = get_date_from_file(file_path2)

    result = get_diff_result_str(first_file, second_file)
    return result


def get_str(sign, key, value):
    return f'  {sign} {key}: {value}\n'


def get_diff_result_str(first_file, second_file):
    all_keys = list(first_file.keys()) + list(second_file.keys())
    result = []
    for key in sorted(set(all_keys)):
        value_1, value_2 = first_file.get(key), second_file.get(key)
        if value_1 is None:
            result.append(get_str('+', key, value_2))
        elif value_2 is None:
            result.append(get_str('-', key, value_1))
        elif value_1 == value_2:
            result.append(get_str(' ', key, value_1))
        else:
            result.append(get_str('-', key, value_1))
            result.append(get_str('+', key, value_2))

    return '{\n' + "".join(result) + '}'
