"""

    *Minor 6th*

  The minor sixth diatonic interval.

"""

from dataclasses import dataclass

from fivear.musical.scale import Diatonic

from ...simple import SimpleInterval

__all__ = ["MinorSixth"]


@dataclass
class MinorSixth(
    SimpleInterval,
    Diatonic,
):
    pass
