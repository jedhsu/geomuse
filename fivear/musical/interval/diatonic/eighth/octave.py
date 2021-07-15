"""

    *Octave*

"""

from dataclasses import dataclass

from fivear.musical.scale import Diatonic

from ..._ordering import SimpleInterval

__all__ = ["PerfectFifth"]


@dataclass
class Octave(
    SimpleInterval,
    Diatonic,
):
    pass
