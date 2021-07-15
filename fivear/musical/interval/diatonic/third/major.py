"""

    *Major 3rd*

  The major third diatonic interval.

"""

from dataclasses import dataclass

from fivear.musical.scale import Diatonic

from ...simple import SimpleInterval

__all__ = ["MajorThird"]


@dataclass
class MajorThird(
    SimpleInterval,
    Diatonic,
):
    pass
