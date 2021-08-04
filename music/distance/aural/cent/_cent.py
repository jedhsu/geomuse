"""

    *Cent*

"""

from .._interval import Interval

__all__ = ["Cent"]


class Cent(
    int,
    Interval,
):
    def __init__(
        self,
        val: int,
    ):
        super(Cent, self).__new__(
            int,
            val,
        )
