"""

    *Octave*

"""

from dataclasses import dataclass

from fivear.musical.scale import Diatonic

from ...simple import SimpleInterval

__all__ = ["Octave"]


@dataclass
class Octave(
    SimpleInterval,
    Diatonic,
):
    pass
