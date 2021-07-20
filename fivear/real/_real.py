"""

    *Real*

  A real musical number.

  Implemented with float.

"""

from abc import ABCMeta

from fivear._number import Number

__all__ = ["RealNumber"]


class RealNumber(
    float,
    Number,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        n: float,
    ):
        super(RealNumber, self).__new__(
            float,
            n,
        )
