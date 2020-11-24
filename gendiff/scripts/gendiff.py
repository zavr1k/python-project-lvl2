import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser("Generate diff")

    parser.add_argument('first_file', type=str,
                        help="Path to the first file")
    parser.add_argument('second_file', type=str,
                        help="Path to the second file")
    parser.add_argument("--format", "-f",
                        help="Set format of output")

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
