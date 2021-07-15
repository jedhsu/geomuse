"""

    *minor 7th*

  The minor 7th diatonic interval.

"""

from dataclasses import dataclass

from fivear.musical.scale import Diatonic

from ...simple import SimpleInterval

__all__ = ["MinorSeventh"]


@dataclass
class MinorSeventh(
    SimpleInterval,
    Diatonic,
):
    pass
