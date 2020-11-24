import argparse


def main():
    parser = argparse.ArgumentParser("Generate diff")

    parser.add_argument('first_file', type=str, help="Path to the first file")
    parser.add_argument('second_file', type=str, help="Path to the second file")

    args = parser.parse_args()


if __name__ == '__main__':
    main()
