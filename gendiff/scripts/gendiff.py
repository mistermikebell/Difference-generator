import argparse

from gendiff.diff_generator import gen_diff
from gendiff.formaters.format import choose


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        type=choose,
        default='stylish',
        help='set format of output')
    args = parser.parse_args()
    diff = gen_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
