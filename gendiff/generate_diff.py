from gendiff.formatter.stylish import get_result_str
from gendiff.parser import get_date_from_file


def generate_diff(file_path1, file_path2):
    first_file_data = get_date_from_file(file_path1)
    second_file_data = get_date_from_file(file_path2)

    result_diff = get_diff_data(first_file_data, second_file_data)
    result = get_result_str(result_diff)
    return result


def get_res_dict(data):
    keys = data.keys()
    res_dict = {}
    for key in keys:
        value = data.get(key)

        if isinstance(value, dict):
            value = get_res_dict(value)
        res_dict[key] = {'action': 'no_modife', 'value': value}
    return res_dict


def get_diff_data(data1, data2):
    keys1 = data1.keys()
    keys2 = data2.keys()
    all_keys = keys1 | keys2

    add_keys = keys2 - keys1
    del_keys = keys1 - keys2
    keys_in_two_dict = keys1 & keys2

    diff_dict = {}

    for key in all_keys:
        value_1, value_2 = data1.get(key), data2.get(key)

        if isinstance(value_1, dict) and isinstance(value_2, dict):
            diff_dict[key] = {
                'action': 'value_dict',
                'value': get_diff_data(value_1, value_2)
            }
        else:
            if isinstance(value_1, dict):
                value_1 = get_res_dict(value_1)
            if isinstance(value_2, dict):
                value_2 = get_res_dict(value_2)

            if key in add_keys:
                diff_dict[key] = {'action': 'add', 'value': value_2}

            if key in del_keys:
                diff_dict[key] = {'action': 'del', 'value': value_1}

            if key in keys_in_two_dict:

                if data1[key] == data2[key]:
                    diff_dict[key] = {'action': 'no_modife', 'value': value_2}

                if data1[key] != data2[key]:
                    diff_dict[key] = {'action': 'modife',
                                      'old_value': value_1,
                                      'new_value': value_2}

    return diff_dict
