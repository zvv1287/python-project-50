

def get_str(action, path, value, new_value=None):

    if action == 'add':
        return f"Property '{path}' was added with value: {value}"

    if action == 'del':
        return f"Property '{path}' was removed"

    if action == 'modife':
        return f"Property '{path}' was updated. From {value} to {new_value}"

    if action == 'value_dict':
        return f"Property '{path}' was added with value: {value}"


def check_and_get_true_value(value):
    if isinstance(value, dict):
        return '[complex value]'

    elif value is True:
        return 'true'

    elif value is False:
        return 'false'

    elif value is None:
        return 'null'

    elif isinstance(value, str):
        return f"'{value}'"

    return value


def get_plain_result_str(diff_data, start_path=''):

    res_str = []
    for key in sorted(diff_data):
        path = start_path + key
        diff_dict = diff_data[key]
        action = diff_dict['action']
        if action == 'value_dict':

            value = diff_dict['value']
            res = get_plain_result_str(value, start_path=path + '.')
            res_str.append(res)

        elif action == 'modife':
            value = check_and_get_true_value(diff_dict['old_value'])
            new_value = check_and_get_true_value(diff_dict['new_value'])

            res = get_str(action, path, value, new_value)
            res_str.append(res)

        elif action == 'add':
            value = diff_dict['value']
            value = check_and_get_true_value(value)
            res = get_str(action, path, value)
            res_str.append(res)

        elif action == 'del':
            value = diff_dict['value']
            res = get_str(action, path, value)
            res_str.append(res)

    return "\n".join(res_str)
