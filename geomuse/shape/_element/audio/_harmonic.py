"""

    *Harmonic*

  Integer multiples of the fundamental frequency.

"""

from dataclasses import dataclass

from fivear.spectral import AudioFrequency
from fivear.spectral import FundamentalFrequency

__all__ = ["Harmonic"]


@dataclass
class Harmonic(
    AudioFrequency,
):
    index: int
    fundamental: FundamentalFrequency

    def __init__(
        self,
        index: int,
        value: float,
    ):
        self.index = index
        super(Harmonic, self).__init__(
            value,
        )
