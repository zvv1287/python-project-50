def main():
    from gendiff.cli import parse_args
    from gendiff.generate_diff import generate_diff

    args = parse_args()
    res = generate_diff(args.first_file, args.second_file, args.format)
    with open('gendiff/files/my_result', 'w') as file:
        file.write(res)

    # with open('gendiff/files/resdiffnew', 'r') as file:
    #     true_res = file.read()
    # print(true_res == res)
    # print('----------------------------------------------')
    # print(res)


if __name__ == '__main__':
    main()
