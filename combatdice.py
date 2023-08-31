
import random
from functools import reduce
from dataclasses import dataclass
from collections.abc import Iterable, Mapping
from utils import find_nth, replace_slice
from common import OutFormat
from typing import Optional, Self

@dataclass
class Roll:
    """
    Represents the result of rolling one or more Fallout Combat Dice.
    """

    damage: int = 0
    effects: int = 0

    def __add__(self, other: 'Roll') -> 'Roll':
        return Roll(self.damage + other.damage, self.effects + other.effects)
    
    def __radd__(self, other: 'Roll') -> 'Roll':
        return self + other

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.damage}, {self.effects})'

    def __str__(self) -> str:
        return f'Damage: {self.damage}, Effects: {self.effects}'

    def __format__(self, spec: str) -> str:
        return self.__str__().__format__(spec)
    
    def __hash__(self) -> int:
        return hash((self.damage, self.effects))


ASCII_FACE_STRINGS = {
    Roll(1, 0): '.',
    Roll(2, 0): ':',
    Roll(0, 0): ' ',
    Roll(1, 1): 'O'
}

UNICODE_FACE_STRINGS = {
    Roll(1, 0): '\u2022', # Bullet
    Roll(2, 0): '\u2821', # Braille Pattern Dots-16
    Roll(0, 0): ' ',
    Roll(1, 1): '\u263A' # White Smiling Face
}


class RollResult:
    """
    Groups multiple rolls of combat dice together to allow for inspection of both the total rolled
    and the individual rolls.
    """

    def __init__(self, rolls: Iterable[Roll]):
        if not isinstance(rolls, Iterable):
            raise TypeError('rolls must be an Iterable')

        roll_list = list(rolls)

        if not all(isinstance(roll, Roll) for roll in roll_list):
            raise TypeError('rolls must iterate over Rolls')

        self.__rolls = roll_list
        self.__total = reduce(lambda x, y: x + y, self.__rolls, Roll())

    @property
    def total(self) -> Roll:
        return self.__total

    @property
    def rolls(self) -> list[Roll]:
        return self.__rolls

    @property
    def effect_triggered(self) -> bool:
        """
        True if the roll had any effect triggered, False otherwise.
        """
        return self.__total.effects > 0


    def rolls_string(self, glyphs_map: Optional[Mapping[Roll, str]] = None) -> str:
        strings: list[str] = []
        if glyphs_map is not None:
            strings = [f'[{glyphs_map.get(roll, f"{roll.damage} {roll.effects}")}]' for roll in self.__rolls]
        else:
            strings = [f'[{roll.damage} {roll.effects}]' for roll in self.__rolls]
        return ' '.join(strings)


    def report_string(self, format: OutFormat, underline_indeces: Optional[Iterable[int]] = None) -> str:
        """
        A string listing of all individual dice rolls and the total result.
        """
        glyphs_map: Optional[dict[Roll, str]] = None
        match format:
            case OutFormat.UNICODE:
                glyphs_map = UNICODE_FACE_STRINGS
            case OutFormat.ASCII:
                glyphs_map = ASCII_FACE_STRINGS
            case OutFormat.NUMERIC:
                pass
        
        report = f'Rolls: {self.rolls_string(glyphs_map)}\n'
        if underline_indeces is not None:
            underline = (' ' * (len(report) - 1)) + '\n'
            for idx in underline_indeces:
                start_idx = find_nth(report, '[', idx + 1)
                end_idx = find_nth(report, ']', idx + 1)
                underline = replace_slice(underline, '^', start_idx, end_idx)
            report += underline
        report += f'Total damage: {self.__total.damage}\n'
        if self.effect_triggered:
            report += f'Total effects: {self.__total.effects}'
        else:
            report += f'No effects'
        return report

    def serialize(self) -> str:
        return ','.join(f'{roll.damage}:{roll.effects}' for roll in self.__rolls)

    @classmethod
    def deserialize(cls, string: str) -> Self:
        return cls(Roll(*map(int, roll.split(':'))) for roll in string.split(','))

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({repr(self.__rolls)})'

    def __str__(self) -> str:
        return str(self.__total)

    def __format__(self, spec: str) -> str:
        return self.__str__().__format__(spec)


class CombatDice:
    """
    Static class used for rolling Fallout Combat Dice and converting regular d6 rolls.
    Should not be instantiated.
    """

    # The values of the faces on a Fallout Combat Dice
    __FACES = [
        Roll(1), 
        Roll(2), 
        Roll(0), 
        Roll(0), 
        Roll(1, 1), 
        Roll(1, 1) 
    ]

    @classmethod
    def roll_single(cls) -> Roll:
        """
        Rolls a single combat die.
        """

        return random.choice(cls.__FACES)
    
    @classmethod
    def roll(cls, number_of_dice: int = 1) -> RollResult:
        """
        Rolls a given number of combat dice and returns the result.
        """

        if not isinstance(number_of_dice, int):
            raise TypeError('number_of_dice must be an integer')
        if number_of_dice < 1:
            raise ValueError('The number of dice rolled must be a non-zero positive integer')

        return RollResult(cls.roll_single() for _ in range(number_of_dice))

    @classmethod
    def from_dice_roll(cls, roll: int) -> Roll:
        """
        Converts a single roll on a d6 into its respective roll on a combat die, as defined in 
        the conversion table in the Fallout TTRPG rulebook.
        """

        if not isinstance(roll, int):
            raise TypeError('roll must be an integer')
        if roll not in range(1, len(cls.__FACES) + 1):
            raise ValueError(f'roll must be in the range [1..{len(cls.__FACES)}]')

        return cls.__FACES[roll - 1]

    @classmethod
    def from_dice_rolls(cls, rolls: Iterable[int]) -> RollResult:
        """
        Converts multiple d6 dice rolls to their respective rolls on combat dice and returns the 
        total result.
        """

        if not isinstance(rolls, Iterable):
            raise TypeError('rolls must be an iterable')

        return RollResult(cls.from_dice_roll(roll) for roll in rolls)
    
