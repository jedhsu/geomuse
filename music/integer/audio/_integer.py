"""

    *Audio Integer*

  An audio integer.

  Commonly known as pitch.

"""

from abc import ABCMeta
from dataclasses import dataclass

from fivear.class_.audio import AudioClass

from .._integer import Integer


__all__ = ["AudioInteger"]


@dataclass
class AudioInteger(
    Integer,
):
    __metaclass__ = ABCMeta

    intclass: AudioClass
    level: int

    def __init__(
        self,
        intclass: AudioClass,
        level: int,
        integer: int,
    ):
        self.intclass = intclass
        self.level = level
        super(AudioInteger, self).__init__(
            integer,
        )
