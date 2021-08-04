"""

    *Decibel - Convert - From*

"""


from ...amplitude._amplitude import Amplitude
from ...power._power import Power

from .._decibel import Decibel

from math import log

__all__ = ["From"]

# [TODO] relative db vs absolute db?


class From:
    @staticmethod
    def from_amplitude(
        ampl: Amplitude,
    ) -> Decibel:
        return Decibel(
            20
            * log(
                ampl,
                10,
            )
        )

    @staticmethod
    def from_power(
        power: Power,
    ) -> Decibel:
        return Decibel(power ** 2)

    @staticmethod
    def from_ratio(
        db: Decibel,
        ratio: float,
    ):
        """
        Percentage greater or smaller.

        Absolute calculation.

        Is this Absolute db or relative db.

        # [TODO] this isnt quite right.... review
        """
        return db + Decibel.from_power(db.into_power() * ratio)

    # def from_phon(self, f: Frequency):
    #     pass
