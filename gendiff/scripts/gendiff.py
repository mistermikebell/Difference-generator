from gendiff.cli import get_parse_args
from gendiff import generate_diff


def main():
    args = get_parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
