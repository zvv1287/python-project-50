import json

def get_date_from_file(file_name):
    DIR_WORK_FILES = 'gendiff/files/'
    return json.load(open(f'{DIR_WORK_FILES}{file_name}'))



def main(name_1, name_2):
    first_file = get_date_from_file(name_1)
    second_file = get_date_from_file(name_2)
    print(first_file)
    print(second_file)





# def get_str(znak, key, value):
#     return f'  {znak} {key}: {value}\n'
#
# def main():
#     from gendiff.worcing.generate_diff import get_date_from_file
#     file_1 = get_date_from_file('gendiff/files/file1.json')
#     file_2 = get_date_from_file('gendiff/files/file2.json')
#     all_keys = list(file_1.keys()) + list(file_2.keys())
#     all_keys = set(all_keys)
#     result = ''
#     for key in sorted(all_keys):
#         value_1, value_2 = file_1.get(key), file_2.get(key)
#         if value_1 is None:
#             result += get_str('+', key, value_2)
#         elif value_2 is None:
#             result += get_str('-', key, value_1)
#         elif value_1 == value_2:
#             result += get_str(' ', key, value_1)
#         else:
#             result += get_str('-', key, value_1)
#             result += get_str('+', key, value_2)
#
#     result = '{\n' + result + '}'
#     return result


'''    
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
'''
