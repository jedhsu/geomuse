"""

    *Coordinate*

  A point imbued with a coordinate system.

"""

from music.__model._spacetime import Point

from music.__model._number import AuralNumber
from music.__model._number import TemporalNumber

__all__ = ["Coordinate"]


class Coordinate(
    Point,
):
    def __init__(
        self,
        f: AuralNumber,
        t: TemporalNumber,
    ):
        super(Coordinate, self).__init__(
            f,
            t,
        )
