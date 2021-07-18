"""

    *Chord*

"""

from typing import Sequence
from typing import TypeVar
from typing import Generic

from fivear.interval import Interval

__all__ = ["Chord"]


class Chord(
    tuple[Interval],
):
    def __init__(
        self,
        intervals: Sequence[Interval],
    ):
        super(Chord, self).__new__(
            tuple,
            intervals,
        )
