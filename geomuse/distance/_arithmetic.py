"""

    *Interval,   [Arithmetic Interface]*

  Interval arithmetic.

"""

from ._interval import Interval

__all__ = ["IntervalArithmetic"]


class IntervalArithmetic(
    Interval,
):
    def __add__(
        self,
        it: Interval,
    ) -> Interval:
        return Interval(self.steps + it.steps)

    def __sub__(
        self,
        it: Interval,
    ) -> Interval:
        return Interval(self.steps - it.steps)
