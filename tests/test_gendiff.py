from gendiff.generate_diff import (
    generate_diff,
    get_date_from_file,
    get_diff_result_str,
    get_str,
)
from gendiff.scripts.gendiff import main


def test_main():
    assert main() == 5


def get_test_data_path(filename):
    from pathlib import Path
    return Path(__file__).parent / 'test_data' / filename


def test_get_date_from_file():
    assert (get_date_from_file(get_test_data_path('file1.json'))
            == {'host': 'hexlet.io', 'timeout': 50,
                'proxy': '123.234.53.22', 'follow': False})


def test_get_diff_result_str():
    first_file = get_date_from_file(get_test_data_path('file1.json'))
    second_file = get_date_from_file(get_test_data_path('file2.json'))
    resdiff = get_test_data_path('resdiff').read_text()

    assert get_diff_result_str(first_file, second_file) == resdiff


def test_get_str():
    assert get_str('+', 'timeout', 20) == '  + timeout: 20\n'


def test_generate_diff():
    file_path_1 = get_test_data_path('file1.json')
    file_path_2 = get_test_data_path('file2.json')
    resdiff = get_test_data_path('resdiff').read_text()

    assert generate_diff(file_path_1, file_path_2) == resdiff
