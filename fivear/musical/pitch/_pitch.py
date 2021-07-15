"""

    *Pitch*

"""

from abc import ABCMeta
from dataclasses import dataclass

from fivear.frequency import AudioFrequency

from ..key import Key

__all__ = ["Pitch"]


@dataclass
class Pitch(
    AudioFrequency,
):
    __metaclass__ = ABCMeta

    key: Key  # this is really a level measure of key, KeyLevel
    level: int
    cents: int

    def __init__(
        self,
        frequency: AudioFrequency,
        key: Key,
        level: int,
        cents: int,
    ):
        self.key = key
        self.level = level
        self.cents = cents

        super(Pitch, self).__init__(
            frequency,
        )
