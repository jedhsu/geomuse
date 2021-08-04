"""

    *Reference Point*

  A point that serves as a frame of reference.

"""

from music.__model._spacetime import Point

from music.__model._number import AuralNumber
from music.__model._number import TemporalNumber

__all__ = ["ReferencePoint"]


class ReferencePoint(
    Point,
):
    def __init__(
        self,
        f: AuralNumber,
        t: TemporalNumber,
    ):
        super(ReferencePoint, self).__init__(
            f,
            t,
        )
