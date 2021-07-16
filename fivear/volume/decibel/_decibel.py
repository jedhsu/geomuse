"""

    *Decibel*

"""

from dataclasses import dataclass

from .._volume import Volume


@dataclass
class Decibel(
    float,
    Volume,
):
    def __init__(
        self,
        val: float,
    ):
        assert val >= 0.0, ValueError("Decibels must be lower than 0.")
        super(Decibel, self).__new__(
            float,
            val,
        )
