import argparse
from gendiff.format.json import transform as transform_json
from gendiff.format.plain import transform as transform_plain
from gendiff.format.stylish import transform as transform_stylish


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
        return transform_stylish(diff)
    if style == 'plain':
        return transform_plain(diff)
    if style == 'json':
        return transform_json(diff)
