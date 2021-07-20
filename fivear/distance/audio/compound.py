"""

    *Compound Interval*

  An interval that is greater than an octave.

"""

from dataclasses import dataclass

from ._interval import Interval
from .simple import SimpleInterval

__all__ = ["CompoundInterval"]


@dataclass
class CompoundInterval(
    Interval,
):
    octaves: int
    simple: SimpleInterval

    def __init__(
        self,
        octaves: int,
        simple: SimpleInterval,
    ):
        assert octaves != 0
        self.octaves = octaves
        self.simple = simple
