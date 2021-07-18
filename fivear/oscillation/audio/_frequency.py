"""

    *Audio-Frequency*

"""

__all__ = ["AudioFrequency"]

from ..frequency import Frequency


class AudioFrequency(
    Frequency,
):
    def __init__(
        self,
        value: float,
    ):
        super(AudioFrequency, self).__init__(
            value,
        )
