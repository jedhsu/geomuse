from __future__ import annotations
from dataclasses import dataclass

from ..time import Duration
from .base import AngularFrequency, Radians


class _Set_:
    def _set(self, val: float):
        self._value = val


@dataclass
class _Frequency(_Set_):
    _value: float


class _Mutate_(_Frequency):
    def mutate_frequency(self, val: float):
        self._set(val)


class _From_(float):
    ...


class _Into_(float):
    def into_angular_frequency(self) -> AngularFrequency:
        ...

    def into_radians(self) -> Radians:
        ...

    def into_period(self) -> Duration:
        return Duration(1 / self)


class _Convert_(
    _From_,
    _Into_,
):
    def from_angular_frequency(self):
        ...


class _Display_(_Frequency):
    unit = "Hz"

    def __repr__(self) -> str:
        return f"{self._value} {self.unit}"


class Frequency(
    float,
):
    def __init__(
        self,
        value: float,
    ):
        super(Frequency, self).__new__(
            float,
            value,
        )
