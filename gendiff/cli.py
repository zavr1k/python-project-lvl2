import argparse
from gendiff.format.json import format_json
from gendiff.format.plain import format_plain
from gendiff.format.stylish import format_stylish


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


def formatter(diff, style='stylish'):
    if style == 'stylish':
        return format_stylish(diff)
    if style == 'plain':
        return format_plain(diff)
    if style == 'json':
        return format_json(diff)
