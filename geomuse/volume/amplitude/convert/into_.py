"""

    *Amplitude - Convert - Into*

"""

from ...decibel._decibel import Decibel
from ...power._power import Power
from .._amplitude import Amplitude

from math import log

__all__ = ["Into"]


class Into(
    Amplitude,
):
    def into_decibel(self) -> Decibel:
        return Decibel(20 * log(self, 10))

    def into_power(self) -> Power:
        return Power(10 * log(self, 10))
