import sys
from argparse import ArgumentParser
from utils import bounded_int
from combatdice import CombatDice
from common import add_common_arguments

def main():
    parser = ArgumentParser(
        description='Converts a list of d6 rolls to their respective combat dice rolls and yields a combined result'
    )
    parser.add_argument(
        'roll', 
        type=bounded_int(1, 6),
        nargs='+',
        metavar='ROLL',
        help='A roll on a d6'
    )
    add_common_arguments(parser, 'history_file', 'out_format')
    args = parser.parse_args()

    result = CombatDice.from_dice_rolls(args.roll)
    with open(args.history_file, 'a') as history:
        history.write(f'{result.serialize()}\n')
    print(result.report_string(args.out_format))

    sys.exit()

if __name__ == '__main__':
    main()