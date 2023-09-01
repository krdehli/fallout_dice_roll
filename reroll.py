import sys
import os
from argparse import ArgumentParser
from combatdice import RollResult, Roll, CombatDice
from common import add_common_arguments
from utils import bounded_int, non_zero_int
from collections.abc import Iterable

def reroll(result: RollResult, indeces: Iterable[int]) -> RollResult:
    new_rolls: list[Roll] = result.rolls.copy()
    for idx in indeces:
        new_rolls[idx] = CombatDice.roll_single()
    return RollResult(new_rolls)

def main():
    parser = ArgumentParser(
        description='Rerolls a Fallout Combat Dice roll from your roll history'
    )
    parser.add_argument(
        'dice_indeces',
        type=bounded_int(1, None),
        nargs='+',
        metavar='DICE_INDECES',
        help='Indeces of the dice to reroll.'
    )
    parser.add_argument(
        '-r','--roll_index',
        type=non_zero_int,
        metavar='ROLL_INDEX',
        help='Non-zero index of the roll to reroll. Negative indeces count backwards from the most recent roll.',
        default=-1
    )
    add_common_arguments(parser, 'history_file', 'out_format')
    args = parser.parse_args()

    history: list[RollResult] = []
    try:
        with open(args.history_file, 'r') as roll_history:
            history = [RollResult.deserialize(line) for line in roll_history.readlines()]
    except FileNotFoundError:
        pass

    idx = args.roll_index
    if idx > 0:
        idx -= 1        

    try:
        result = reroll(history[idx], map(lambda i: i - 1, args.dice_indeces))
        with open(args.history_file, 'a') as roll_history:
            roll_history.write(f'{result.serialize()}\n')
        print(result.report_string(args.out_format, map(lambda i: i - 1, args.dice_indeces)))
        
    except Exception as e:
        parser.print_usage()
        print(f'{os.path.basename(__file__)}: error: {e}')
        sys.exit(2)

    sys.exit()

if __name__ == '__main__':
    main()
    