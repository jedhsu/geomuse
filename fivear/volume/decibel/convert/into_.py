"""

    *Decibel - Convert - Into*

"""


from ...amplitude._amplitude import Amplitude
from ...power._power import Power

from .._decibel import Decibel

__all__ = ["Into"]


class Into(
    Decibel,
):
    def into_amplitude(self) -> Amplitude:
        return Amplitude(10.0 ** (self / 20))

    def into_power(self) -> Power:
        return Power(self ** 0.5)

    # def into_phon(self, f: Frequency) -> Phon:
    #     # TODO: look at equation
    #     raise NotImplementedError
