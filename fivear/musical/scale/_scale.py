"""

    *Scale*

  A type that is "musically scaled".

  More precisely, a scale is a partition of the octave into n
  equidistant parts.

  # [TODO] better explanation on log equidistance.

"""

from abc import ABCMeta

__all__ = ["Scale"]


class Scale(
    Ring,
):
    __metaclass__ = ABCMeta
