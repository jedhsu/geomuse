"""

    *Audio Real*

  A real number of audio. This is FREQUENCY.

  Need easier notation, shrink words later...

"""

from abc import ABCMeta

from .._real import RealNumber

__all__ = ["AudioReal"]


class AudioReal(
    RealNumber,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        n: float,
    ):
        super(AudioReal, self).__init__(
            n,
        )
