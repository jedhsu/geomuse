"""

    *Perfect 4th*

"""

from dataclasses import dataclass

from fivear.musical.scale import Diatonic

from ..._interval import Interval

__all__ = ["PerfectFourth"]


@dataclass
class PerfectFourth(
    Interval,
    Diatonic,
):
    pass
