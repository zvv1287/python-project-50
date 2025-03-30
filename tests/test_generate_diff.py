from gendiff.generate_diff import generate_diff, get_diff_data, get_res_dict


def get_data_path(filename):
    from pathlib import Path
    return Path(__file__).parent / 'test_data' / filename


def test_generate_diff():
    resdiff = get_data_path('resdiff').read_text()
    file_path_1 = get_data_path('file1.json')
    file_path_2 = get_data_path('file2.json')
    assert generate_diff(file_path_1, file_path_2) == resdiff

    resdiff = get_data_path('resdiffnew').read_text()
    file_path_1 = get_data_path('file1new.json')
    file_path_2 = get_data_path('file2new.json')
    assert generate_diff(file_path_1, file_path_2) == resdiff


def test_get_res_dict():
    data = {'deep': {'id': {'number': 45}}, 'fee': 100500}
    true_res = {'deep':
                    {'action': 'no_modife',
                     'value':
                        {'id': {
                            'action': 'no_modife',
                            'value': {
                                'number': {
                                    'action': 'no_modife',
                                    'value': 45}
                            }
                        }
                        }
                     },
                'fee': {
                    'action': 'no_modife', 'value': 100500}
                }
    assert get_res_dict(data) == true_res


def test_get_diff_data():
    first_file_data = {'key_del': 'hexlet.io', 'key_mod': 50,
                       'key_nothing': 'noth', 'key_dict': {'key': 'value'}}
    second_file_data = {'key_add': 'hexlet', 'key_mod': 20,
                        'key_nothing': 'noth', 'key_dict': {'key2': 'value2'}}

    true_res = \
        {'key_del': {'action': 'del', 'value': 'hexlet.io'},
         'key_dict': {'action': 'value_dict', 'value': {
             'key': {'action': 'del', 'value': 'value'},
             'key2': {'action': 'add', 'value': 'value2'}}},
         'key_add': {'action': 'add', 'value': 'hexlet'},
         'key_mod': {'action': 'modife', 'old_value': 50, 'new_value': 20},
         'key_nothing': {'action': 'no_modife', 'value': 'noth'}}

    assert get_diff_data(first_file_data, second_file_data) == true_res
