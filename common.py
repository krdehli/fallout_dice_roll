from argparse import ArgumentParser
import os
from enum import StrEnum, auto

class OutFormat(StrEnum):
    UNICODE = auto()
    ASCII = auto()
    NUMERIC = auto()

    @classmethod
    def from_str(cls, s: str):
        try:
            return cls(s)
        except ValueError:
            return cls.UNICODE


def add_common_arguments(parser: ArgumentParser, history_file_dest: str = 'history_file', out_format_dest: str = 'out_format'):
    if not isinstance(parser, ArgumentParser):
        raise TypeError('parser must be an ArgumentParser')
    if not isinstance(history_file_dest, str):
        raise TypeError('history_file_dest must be a string')
    if not isinstance(out_format_dest, str):
        raise TypeError('out_format_dest must be a string')
    
    default_history_file = os.environ.get('FALLOUT_DICE_ROLL_HISTORY_FILE', default='./roll_history')
    default_out_format = OutFormat.from_str(os.environ.get('FALLOUT_DICE_ROLL_OUT_FORMAT', default='unicode').lower())

    parser.add_argument(
        '--history_file',
        type=str,
        metavar='FILE',
        help='Path to the file where the roll history is stored',
        default=default_history_file,
        dest=history_file_dest
    )
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument(
        '-a','--ascii',
        action='store_const',
        const=OutFormat.ASCII,
        help='Use ASCII compatible characters for the dice output',
        default=default_out_format,
        dest=out_format_dest
    )
    output_group.add_argument(
        '-n','--numeric',
        action='store_const',
        const=OutFormat.NUMERIC,
        help='Use number pairs instead of characters for the dice output',
        default=default_out_format,
        dest=out_format_dest
    )
    output_group.add_argument(
        '-u','--unicode',
        action='store_const',
        const=OutFormat.UNICODE,
        help='Use unicode characters for the dice output. This is the default behaviour',
        default=default_out_format,
        dest=out_format_dest
    )