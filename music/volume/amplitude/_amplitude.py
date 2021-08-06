"""

    *Amplitude*

  Amplitude, a unit measure of sound volume.

"""

from dataclasses import dataclass

from depyth import Type

from .._volume import Volume

__all__ = ["Amplitude"]


@dataclass
class Amplitude(
    float,
    Volume,
):
    def __init__(
        self,
        val: float,
    ):
        assert 0.0 <= self <= 1.0, ValueError("Amplitude must be between 0 and 1.")

        super(Amplitude, self).__new__(
            float,
            val,
        )
