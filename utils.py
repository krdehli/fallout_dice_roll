from typing import Callable
from argparse import ArgumentTypeError

def bounded_int(lower: int | None, upper: int | None) -> Callable[[str], int]:
    def unbounded(value: str) -> int:
        integer_value = 0
        try:
            integer_value = int(value)
        except:
            raise ArgumentTypeError(f'{value} is not a valid integer')
        return integer_value

    def lower_bounded(value: str) -> int:
        integer_value = unbounded(value)
        assert lower is not None
        if integer_value < lower:
            raise ArgumentTypeError(f'argument must be an integer in the range [{lower}..]')

        return integer_value

    def upper_bounded(value: str) -> int:
        integer_value = unbounded(value)
        assert upper is not None
        if integer_value > upper:
            raise ArgumentTypeError(f'argument must be an integer in the range [..{upper}]')

        return integer_value

    def lower_and_upper_bounded(value: str) -> int:
        integer_value = unbounded(value)
        assert lower is not None and upper is not None
        if integer_value not in range(lower, upper + 1):
            raise ArgumentTypeError(f'argument must be an integer in the range [{lower}..{upper}]')

        return integer_value

    if lower is None and upper is None:
        return unbounded
    elif upper is None:
        return lower_bounded
    elif lower is None:
        return upper_bounded
    else:
        return lower_and_upper_bounded
