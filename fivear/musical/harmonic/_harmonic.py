"""

    *Harmonic*

"""

from dataclasses import dataclass

from fivear.frequency import AudioFrequency

__all__ = ["Harmonic"]


@dataclass
class Harmonic(
    AudioFrequency,
):
    index: int

    def __init__(
        self,
        index: int,
        value: float,
    ):
        self.index = index
        super(Harmonic, self).__init__(
            value,
        )
