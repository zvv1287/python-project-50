import json


def main():
    import argparse

    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )

    parser.add_argument('first_file', type=str, help='Путь к первому файлу')
    parser.add_argument('second_file', type=str, help='Путь ко второму файлу')

    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    return args


def generate_diff(file_path_1, file_path_2):
    dict_1 = json.load(open(file_path_1))
    dict_2 = json.load(open(file_path_2))

    all_keys = dict_1.keys() | dict_2.keys()
    res = []
    for key in sorted(all_keys):
        if key not in dict_1.keys():
            res.append(f'+ {key}: {dict_2[key]}')
        elif key not in dict_2.keys():
            res.append(f'- {key}: {dict_1[key]}')
        elif dict_1[key] == dict_2[key]:
            res.append(f'  {key}: {dict_1[key]}')
        else:
            res.append(f'- {key}: {dict_1[key]}')
            res.append(f'+ {key}: {dict_2[key]}')
    res_string = '\n'.join(res)
    return res_string


if __name__ == '__main__':
    args = main()

    file_path1 = f'gendiff/files/{args.first_file}'
    file_path2 = f'gendiff/files/{args.second_file}'

    with open(file_path1, 'r') as f:
        print("Исходный файл: ", f.read())
    with open(file_path2, 'r') as f:
        print("Файл после изменения: ", f.read())
    diff = generate_diff(file_path1, file_path2)
    print("Сравнение:")
    print(diff)
