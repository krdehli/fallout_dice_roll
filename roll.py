import sys
from combatdice import CombatDice
from utils import bounded_int
from argparse import ArgumentParser

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
    args = parser.parse_args()

    print(CombatDice.roll(args.num_rolls).report_string)
    sys.exit()

if __name__ == '__main__':
    main()
