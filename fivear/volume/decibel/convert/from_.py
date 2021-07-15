"""

    *Decibel - Convert - From*

"""


from ...amplitude._amplitude import Amplitude
from ...power._power import Power

from .._decibel import Decibel

from math import log

__all__ = ["From"]


class From:
    @staticmethod
    def from_amplitude(ampl: Amplitude) -> Decibel:
        return Decibel(20 * log(ampl, 10))

    @staticmethod
    def from_power(power: Power) -> Decibel:
        return Decibel(power ** 2)

    # def from_phon(self, f: Frequency):
    #     pass
