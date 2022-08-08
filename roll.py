import sys
from  combatdice import CombatDice
from argparse import ArgumentParser, ArgumentTypeError

def positive_nonzero_int(value: str) -> int:
    integer_value = 0

    try:
        integer_value = int(value)
    except:
        raise ArgumentTypeError(f'{value} is not a valid integer')

    if integer_value < 1:
        raise ArgumentTypeError('argument must be a positive non-zero integer')

    return integer_value

def main():
    parser = ArgumentParser(
        description='Rolls a given number of Fallout Combat Dice and yields a combined result'
    )
    parser.add_argument(
        'num_rolls',
        type=positive_nonzero_int,
        metavar='NUM_ROLLS',
        help='The given number of combat dice to roll'
    )
    args = parser.parse_args()

    print(CombatDice.roll(args.num_rolls))

    sys.exit()

if __name__ == '__main__':
    main()
