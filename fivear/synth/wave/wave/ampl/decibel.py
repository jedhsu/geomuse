"""

    Decibel

  Models decibel.

"""
from __future__ import annotations
from math import log

from ..freq import Frequency
from .base import Amplitude, Phon, Power
from .base import Decibel as _Decibel

__all__ = ["Decibel"]


# [TODO] Validator? not super necessary, do later


class _From_:
    @staticmethod
    def from_amplitude(ampl: Amplitude):
        return _Decibel(20 * log(ampl, 10))

    @staticmethod
    def from_power(power: Power):
        return _Decibel(power ** 2)

    def from_phon(self, f: Frequency):
        pass


class _Into_(_Decibel):
    def into_amplitude(self) -> Amplitude:
        return Amplitude(10.0 ** (self / 20))

    def into_power(self) -> Power:
        return Power(self ** 0.5)

    def into_phon(self, f: Frequency) -> Phon:
        # TODO: look at equation
        raise NotImplementedError


class _Convert_(
    _From_,
    _Into_,
):
    pass


class _Unit_:
    unit = None  # [TODO] confirm this is no units


class _Display_(_Unit_):
    def __repr__(self) -> str:
        number = f"{self:.3f}"
        return f"{number} {self.unit}" if self.unit else number


class Decibel(
    _Display_,
    _Convert_,
    _Decibel,
):
    pass
