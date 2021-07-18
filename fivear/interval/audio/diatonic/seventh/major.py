"""

    *Major 7th*

  The major 7th diatonic interval.

"""

from dataclasses import dataclass

from fivear.musical.scale import Diatonic

from ...simple import SimpleInterval

__all__ = ["MajorSeventh"]


@dataclass
class MajorSeventh(
    SimpleInterval,
    Diatonic,
):
    pass
