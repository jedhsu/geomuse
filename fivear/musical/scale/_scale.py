"""

    *Scale*

  A type that is "musically scaled".

  # [TODO] better explanation.

  # [TODO] is this a mathematical ring?

"""

from abc import ABCMeta

__all__ = ["Scale"]


class Scale(
    Ring,
):
    __metaclass__ = ABCMeta
