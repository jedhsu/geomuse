"""

    Interval,   [Bindings]

"""


from ._interval import Interval as _Interval

from ._arithmetic import IntervalArithmetic
from ._ordering import IntervalOrdering

__all__ = ["Interval"]


class Interval(
    IntervalArithmetic,
    IntervalOrdering,
    _Interval,
):
    pass
