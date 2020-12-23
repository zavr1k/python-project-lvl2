import argparse
from gendiff.format.json import to_json
from gendiff.format.plain import to_plain
from gendiff.format.stylish import stylish


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
        return stylish(diff)
    if style == 'plain':
        return to_plain(diff)
    if style == 'json':
        return to_json(diff)