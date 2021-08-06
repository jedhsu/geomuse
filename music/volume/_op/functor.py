"""

    *Volume Functor*

"""

from .._volume import Volume

from ..amplitude import Amplitude
from ..decibel import Decibel
from ..power import Power
from ..phon import Phon
from ..sone import Sone

__all__ = ["VolumeMorphism"]


class VolumeMorphism(
    Volume,
):
    def as_amplitude(self) -> Amplitude:
        return self.into_amplitude()

    def as_decibels(self) -> Decibel:
        return self.into_decibels()

    def as_power(self) -> Power:
        pass

    def as_phon(self) -> Phon:
        pass

    def as_sone(self) -> Sone:
        pass
