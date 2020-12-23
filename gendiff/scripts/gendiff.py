from gendiff.cli import init_argparse
from gendiff.gendiff import generate_diff


def main():
    parser = init_argparse()
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
