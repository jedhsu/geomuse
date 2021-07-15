"""

    *Major 6th*

  The major sixth diatonic interval.

"""

from dataclasses import dataclass

from fivear.musical.scale import Diatonic

from ...simple import SimpleInterval

__all__ = ["MajorSixth"]


@dataclass
class MajorSixth(
    SimpleInterval,
    Diatonic,
):
    pass
