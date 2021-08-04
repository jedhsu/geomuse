"""

    *Amplitude - Convert - From*

"""

from ...decibel._decibel import Decibel
from ...power._power import Power

from .._amplitude import Amplitude

__all__ = ["From"]


class From:
    @staticmethod
    def from_decibel(db: Decibel) -> Amplitude:
        return Amplitude(10.0 ** (db / 20))

    @staticmethod
    def from_power(pow: Power) -> Amplitude:
        return Amplitude(10.0 ** (pow / 10))
