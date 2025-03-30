INDENT = '    '


def get_str(action, key, value, space_count):
    actions = {'add': '  + ', 'del': '  - ',
               'no_modife': '    ', 'value_dict': '    '}
    sign = actions[action]
    return f'{INDENT * space_count}{sign}{key}: {value}\n'


def check_and_get_true_value(value, space_count):
    if isinstance(value, dict):
        value = get_result_str(value, space_count + 1)
        return value

    if value is True:
        return 'true'

    if value is False:
        return 'false'

    if value is None:
        return 'null'

    return value


def get_result_str(diff_data, space_count=0):
    res_str = []
    for key in sorted(diff_data):
        diff_dict = diff_data[key]
        action = diff_dict['action']
        if action == 'value_dict':
            value_diff_data = diff_dict['value']
            value = get_result_str(value_diff_data, space_count + 1)
            res = get_str(action, key, value, space_count)
            res_str.append(res)

        elif action == 'modife':
            value = diff_dict['old_value']
            value = check_and_get_true_value(value, space_count)
            res = get_str('del', key, value, space_count)
            res_str.append(res)

            value = diff_dict['new_value']
            value = check_and_get_true_value(value, space_count)
            res = get_str('add', key, value, space_count)
            res_str.append(res)

        else:

            value = diff_dict['value']
            value = check_and_get_true_value(value, space_count)
            res = get_str(action, key, value, space_count)
            res_str.append(res)

    return '{\n' + "".join(res_str) + (INDENT * space_count) + '}'
