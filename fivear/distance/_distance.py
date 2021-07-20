"""

    *Distance*

  A measure of distance of musical numbers.

"""

from abc import ABCMeta

from fivear._number import Number

__all__ = ["Distance"]


class Distance(
    Number,
):
    __metaclass__ = ABCMeta
