"""

    *Interval Arithmetic*

"""

from ._interval import Interval

__all__ = ["IntervalArithmetic"]


class IntervalArithmetic(
    Interval,
):
    def __add__(
        self,
        it: Interval,
    ):
        pass

    def __sub__(
        self,
        it: Interval,
    ):
        pass
