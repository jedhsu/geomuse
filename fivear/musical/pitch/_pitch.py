"""

    *Pitch*

"""

from abc import ABCMeta
from dataclasses import dataclass

from fivear.frequency import AudioFrequency


@dataclass
class Pitch:
    __metaclass__ = ABCMeta

    frequency: AudioFrequency
