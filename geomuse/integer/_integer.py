"""

    *Integer*

  An integer of music.

  Implemented with int.

"""

from abc import ABCMeta

from music.__model._number import Number

__all__ = ["Integer"]


class Integer(
    int,
    Number,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        n: int,
    ):
        super(Integer, self).__new__(
            int,
            n,
        )
