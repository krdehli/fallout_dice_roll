
from dataclasses import dataclass
import random
from itertools import count
from collections.abc import Iterable

def roll_d20(number_of_dice: int = 1) -> list[int]:
    """
    Rolls a given number of D20s and returns the results.
    """   

    if not isinstance(number_of_dice, int):
        raise TypeError('number_of_dice must be an integer')
    if number_of_dice < 1:
        raise ValueError('The number of dice rolled must be a non-zero positive integer')

    return [random.randint(1, 20) for _ in range(number_of_dice)]


@dataclass
class TestResult:
    """
    The result of a D20 test
    """

    def __init__(self, rolls: Iterable[int], target_number: int, critical_threshold: int):
        if not isinstance(rolls, Iterable):
            raise TypeError('rolls must be an Iterable')
        
        roll_list = list(rolls)

        if not isinstance(target_number, int):
            raise TypeError('target_number must be an int')
        
        self.__target_number = target_number

        if not isinstance(critical_threshold, int):
            raise TypeError('critical_threshold must be an int')
        
        self.__critical_threshold = critical_threshold

        if not all(isinstance(roll, int) for roll in roll_list):
            raise TypeError('rolls must iterate over int')
        
        if not all(1 <= roll <= 20 for roll in roll_list):
            raise ValueError('roll values must be between 1 and 20')
        
        self.__rolls = roll_list
        self.__critical_successes = 0
        self.__regular_successes = 0
        self.__critical_failures = 0

        for roll in self.__rolls:
            if roll == 20:
                self.__critical_failures += 1
            elif roll <= self.__critical_threshold:
                self.__critical_successes += 1
            elif roll <= self.__target_number:
                self.__regular_successes += 1

    @property
    def rolls(self) -> list[int]:
        return self.__rolls

    @property
    def total_successes(self) -> int:
        return 2 * self.__critical_successes + self.__regular_successes
    
    @property
    def critical_successes(self) -> int:
        return self.__regular_successes
    
    @property 
    def critical_failures(self) -> int:
        return self.__critical_failures
    
    @property
    def has_critical_success(self) -> bool:
        return self.__critical_successes > 0
    
    @property
    def has_critical_faulure(self) -> bool:
        return self.__critical_failures > 0
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({repr(self.__rolls)}, {self.__target_number}, {self.__critical_threshold})'

    def __str__(self) -> str:
        return str(self.total_successes)
    
    def __format__(self, spec: str) -> str:
        return self.total_successes.__format__(spec)
    

def test(target_number: int, number_of_dice: int = 2, critical_threshold: int = 1) -> TestResult:
    """
    Makes a D20 test against the given target number.
    """

    if not isinstance(target_number, int):
        raise TypeError('target_number must be an integer')
    if not isinstance(number_of_dice, int):
        raise TypeError('number_of_dice must be an integer')
    if number_of_dice < 1:
        raise ValueError('The number of dice rolled must be a non-zero positive integer')

    return TestResult(roll_d20(number_of_dice), target_number, critical_threshold)
