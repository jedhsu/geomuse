"""

    *Interval Chord*

  A chord of intervals, which are deltas.

"""

from typing import Sequence

from .._bind import Interval

__all__ = ["IntervalChord"]


class IntervalChord(
    tuple[Interval],
):
    def __init__(
        self,
        intervals: Sequence[Interval],
    ):
        super(IntervalChord, self).__new__(
            tuple,
            intervals,
        )
