"""

    *Perfect 5th*

"""

from dataclasses import dataclass

from fivear.musical.scale import Diatonic

from ...simple import SimpleInterval

__all__ = ["PerfectFifth"]


@dataclass
class PerfectFifth(
    SimpleInterval,
    Diatonic,
):
    pass
