import argparse


def init_argparse():
    parser = argparse.ArgumentParser(description='Generate difference')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('--format', '-f',
                        help='set format of output',
                        default='stylish',
                        choices=['stylish', 'plain', 'json']
                        )
    return parser
