"""

    *Interval,   [Ordering Interface]*

  Defines the total ordering on intervals.

"""

from ._interval import Interval

__all__ = ["IntervalOrdering"]


class IntervalOrdering(
    Interval,
):
    def __lt__(
        self,
        it: Interval,
    ):
        return self.steps < it.steps

    def __le__(
        self,
        it: Interval,
    ):
        return self.steps <= it.steps

    def __gt__(
        self,
        it: Interval,
    ):
        return self.steps > it.steps

    def __ge__(
        self,
        it: Interval,
    ):
        return self.steps >= it.steps
