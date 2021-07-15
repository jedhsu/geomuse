"""

    *Harmonic Series*

"""

from dataclasses import dataclass

from typing import Sequence

from ._harmonic import Harmonic

__all__ = ["Harmonic"]


@dataclass
class HarmonicSeries(
    tuple[Harmonic],
):
    def __init__(
        self,
        harmonics: Sequence[Harmonic],
    ):
        return super(HarmonicSeries, self).__new__(
            tuple,
            harmonics,
        )

    @classmethod
    def create(cls):
        pass
