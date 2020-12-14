import argparse

from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate difference')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('--format', '-f', help='set format of output',
                        default='stylish')

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
