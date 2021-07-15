"""

    *Decibel*

"""

from dataclasses import dataclass


@dataclass
class Decibel(
    float,
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
