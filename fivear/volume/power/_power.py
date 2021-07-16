"""

    *Power*

"""

from dataclasses import dataclass

from .._volume import Volume


@dataclass
class Power(
    float,
    Volume,
):
    def __init__(
        self,
        val: float,
    ):
        # [TODO] confirm
        assert 0.0 <= self <= 1.0, ValueError("Power must be lower than 0.")
        super(Power, self).__new__(
            float,
            val,
        )
