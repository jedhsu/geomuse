"""

    *Point*

  A point in musical spacetime.

"""

from dataclasses import dataclass

from music.__model._number import AuralNumber
from music.__model._number import TemporalNumber

__all__ = ["Point"]


@dataclass
class Point:
    f: AuralNumber
    t: TemporalNumber
