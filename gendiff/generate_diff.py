from gendiff.parser import get_date_from_file


def generate_diff(file_path1, file_path2):
    first_file_data = get_date_from_file(file_path1)
    second_file_data = get_date_from_file(file_path2)

    result_diff = get_diff_result(first_file_data, second_file_data)
    result = get_diff_result_str(first_file_data, second_file_data, result_diff)

    return result


def get_diff_result(first_file, second_file):
    merged_dict = {**first_file, **second_file}
    result_dict = {}
    for key in merged_dict:
        value_1, value_2 = first_file.get(key), second_file.get(key)
        if value_1 is None:
            result_dict[key] = 'add'
        elif value_2 is None:
            result_dict[key] = 'del'
        elif value_1 == value_2:
            result_dict[key] = 'nothing'
        else:
            result_dict[key] = 'changed'

    return result_dict


def get_diff_result_str(first_file_data, second_file_data, result_diff):
    merged_dict = {**first_file_data, **second_file_data}
    result = []
    for key in sorted(merged_dict):
        action = result_diff[key]

        if action == 'changed':
            action = 'del'
            value = first_file_data[key]
            result.append(get_str(action, key, value))
            action = 'add'

        value = merged_dict[key]
        result.append(get_str(action, key, value))
    return '{\n' + "".join(result) + '}'


def get_str(action, key, value):
    actions = {'add': '+', 'del': '-', 'nothing': ' '}
    return f'  {actions[action]} {key}: {value}\n'
