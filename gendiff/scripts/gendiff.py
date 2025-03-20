def main():
    import argparse

    from gendiff.generate_diff import generate_diff

    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()
    res = generate_diff(args.first_file, args.second_file)
    print(res)



if __name__ == '__main__':
    main()
