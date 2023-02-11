from gendiff.scripts.gendiff import generate_diff


def test_func_1():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    with open('tests/fixtures/result.txt', 'r') as f:
        res = f.read()
    print(res)
    assert generate_diff(file_path1, file_path2) == res
