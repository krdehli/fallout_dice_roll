import sys
from argparse import ArgumentParser
from combatdice import CombatDice
from utils import bounded_int
from common import add_common_arguments

def main():
    parser = ArgumentParser(
        description='Rolls a given number of Fallout Combat Dice and yields a combined result'
    )
    parser.add_argument(
        'num_rolls',
        type=bounded_int(1, None),
        metavar='NUM_ROLLS',
        help='The given number of combat dice to roll'
    )
    add_common_arguments(parser, 'history_file', 'out_format')
    args = parser.parse_args()

    result = CombatDice.roll(args.num_rolls)
    with open(args.history_file, 'a') as history:
        history.write(f'{result.serialize()}\n')
    print(result.report_string(args.out_format))
    
    sys.exit()

if __name__ == '__main__':
    main()

