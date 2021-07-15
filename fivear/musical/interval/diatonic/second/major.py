"""

    *Major 2nd*

  The major second interval of the diatonic scale.

    *Whole-Step*

  Also known as the whole step of the diatonic scale.

"""

from dataclasses import dataclass

from fivear.musical.scale import Diatonic

from ...simple import SimpleInterval

__all__ = ["MajorSecond"]


@dataclass
class MajorSecond(
    SimpleInterval,
    Diatonic,
):
    pass
