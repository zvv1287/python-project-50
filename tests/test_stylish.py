from gendiff.formatter.stylish import get_str


def test_get_str():
    true_res = '      + setting3: null\n'
    assert get_str('add', 'setting3', 'null', 1) == true_res

    true_res = '    host: hexlet.io\n'
    assert get_str('no_modife', 'host', 'hexlet.io', 0) == true_res
