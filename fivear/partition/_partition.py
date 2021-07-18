"""

    *Scale*

  A type that is "musically scaled".

  More precisely, a scale is a partition of the octave into n
  equidistant parts.

  # [TODO] better explanation on log equidistance.

  does scale have a time analog?

"""

from abc import ABCMeta
from dataclasses import dataclass

__all__ = ["Scale"]


@dataclass
class Scale(
    # Ring,
):
    __metaclass__ = ABCMeta

    elements: int
