from gendiff.parser import get_date_from_file, get_file_date


def get_data_path(filename):
    from pathlib import Path
    return Path(__file__).parent / 'test_data' / filename


def test_get_file_date():
    path = get_data_path('file1.json')

    assert get_file_date(path) == '''{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}'''


def test_get_date_from_file():
    assert (get_date_from_file(get_data_path('file1.json'))
            == {'host': 'hexlet.io', 'timeout': 50,
                'proxy': '123.234.53.22', 'follow': False})
    assert (get_date_from_file(get_data_path('file1.yml'))
            == {'host': 'hexlet.io', 'timeout': 50,
                'proxy': '123.234.53.22', 'follow': False})
    assert (get_date_from_file(get_data_path('file2.yaml'))
            == {'host': 'hexlet.io', 'timeout': 20,
                'verbose': True})
