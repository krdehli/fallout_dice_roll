import sys
import os
import io
from argparse import ArgumentParser
from combatdice import RollResult
from common import add_common_arguments, OutFormat

def display(history_file: io.TextIOWrapper, out_format: OutFormat):
    if not isinstance(history_file, io.TextIOWrapper):
        raise TypeError('history_file must be a io.TextIOWrapper')
    if not history_file.readable():
        raise ValueError('history_file must be readable')
    
    for idx, line in enumerate(history_file):
        print(f'* Roll #{idx + 1} *')
        print(RollResult.deserialize(line).report_string(out_format))
        print('***\n')


def clear(history_file: io.TextIOWrapper):
    if not isinstance(history_file, io.TextIOWrapper):
        raise TypeError('history_file must be a io.TextIOWrapper')
    if not history_file.writable():
        raise ValueError('history_file must be writable')
    
    input_accepted = False
    while not input_accepted:
        confirm = input('Are you sure you want to clear the entire roll history? ([y]es/[n]o): ')
        if confirm.lower() in ['yes', 'y']:
            history_file.truncate(0)
            input_accepted = True
        elif confirm.lower() in ['no', 'n']:
            input_accepted = True
        else:
            print(f'unrecognized input: "{confirm}"')


def main():
    parser = ArgumentParser(
        description='Lists your roll history'
    )
    parser.add_argument(
        '--clear',
        action='store_true',
        help="Clears the entire history file"
    )
    add_common_arguments(parser, 'history_file', 'out_format')
    args = parser.parse_args()

    try:
        if args.clear:
            with open(args.history_file, 'r+') as file:
                clear(file)
        else:
            with open(args.history_file, 'r') as file:
                display(file, args.out_format)
    except FileNotFoundError:
        pass
   
    sys.exit()

if __name__ == '__main__':
    main()