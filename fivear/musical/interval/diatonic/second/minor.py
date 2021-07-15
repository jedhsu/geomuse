"""

    *Minor 2nd*

  The major second interval of the diatonic scale.

    *Half-Step*

  Also known as the half step of the diatonic scale.

    *Semitone*

  Also known as the semitone.

"""

from dataclasses import dataclass

from fivear.musical.scale import Diatonic

from ...simple import SimpleInterval

__all__ = ["MinorSecond"]


@dataclass
class MinorSecond(
    SimpleInterval,
    Diatonic,
):
    pass
