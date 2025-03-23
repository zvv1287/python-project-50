def main():
    from gendiff.cli import parse_args
    from gendiff.generate_diff import generate_diff

    args = parse_args()
    res = generate_diff(args.first_file, args.second_file)
    print(res)


if __name__ == '__main__':
    main()
