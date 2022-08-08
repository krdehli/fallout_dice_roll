import sys
from argparse import ArgumentParser, ArgumentTypeError
from typing import Callable
from combatdice import CombatDice

def bounded_int(lower: int, upper: int) -> Callable[[str], int]:
    def inner(value: str) -> int:
        integer_value = 0
        try:
            integer_value = int(value)
        except:
            raise ArgumentTypeError(f'{value} is not a valid integer')

        if integer_value not in range(lower, upper + 1):
            raise ArgumentTypeError(f'argument must be an integer in the range [{lower}..{upper}]')

        return integer_value

    return inner

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

    print(CombatDice.from_dice_rolls(args.roll))
    sys.exit()

if __name__ == '__main__':
    main()