"""

    *Partition*

  A type that is "musically scaled".

  This is commonly scale, and there can be temporal scale as well!

  More precisely, a scale is a partition of the octave into n
  equidistant parts.

  # [TODO] better explanation on log equidistance.

  does scale have a time analog?

"""

from abc import ABCMeta
from dataclasses import dataclass

__all__ = ["Partition"]


@dataclass
class Partition(
    # Ring,
):
    __metaclass__ = ABCMeta

    elements: int
