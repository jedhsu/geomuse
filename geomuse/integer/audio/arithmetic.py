"""

    *Pitch Arithmetic*

"""

from ..interval import Interval

from ._pitch import Pitch

__all__ = ["PitchArithmetic"]


class PitchArithmetic(
    Pitch,
):
    def __add__(
        self,
        it: Interval,
    ) -> Pitch:
        """
        Add an interval to a pitch to get a pitch.
        """
        assert isinstance(it, Interval)
        raise NotImplementedError

    def __sub__(
        self,
        pitch: Pitch,
    ) -> Interval:
        """
        Subtract a pitch to a pitch to get an interval.

        """
        assert isinstance(pitch, Pitch)
