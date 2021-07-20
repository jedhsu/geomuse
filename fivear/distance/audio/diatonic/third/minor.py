"""

    *Minor 3rd*

  The minor third diatonic interval.

"""

from dataclasses import dataclass

from fivear.musical.scale import Diatonic

from ...simple import SimpleInterval

__all__ = ["MinorThird"]


@dataclass
class MinorThird(
    SimpleInterval,
    Diatonic,
):
    pass
