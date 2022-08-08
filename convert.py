import sys
from argparse import ArgumentParser
from utils import bounded_int
from combatdice import CombatDice

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
    args = parser.parse_args()

    print(CombatDice.from_dice_rolls(args.roll).report_string)
    sys.exit()

if __name__ == '__main__':
    main()