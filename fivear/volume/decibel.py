"""

    Reference Decibel

  Models sound intensity. Reference level is 0 db.

"""

from __future__ import annotations
from math import log

from .base import Amplitude, Power
from .base import Decibel as _Decibel

__all__ = ["Decibel"]


class _Validate_(_Decibel):
    def validate(self) -> bool:
        """
        Validates decibel value as negative.

        """
        if self >= 0.0:
            raise ValueError("Decibels must be lower than 0.")

        return True


class _Convert_(
    _From_,
    _Into_,
):
    pass


class _Unit_:
    unit = "db"


class _Display_(_Unit_):
    def __repr__(self) -> str:
        number = f"{self:.2f}"
        return f"{number} {self.unit}" if self.unit is not None else number


class Decibel(
    _Display_,
    _Convert_,
    _Validate_,
    _Decibel,
):
    def __init__(self, val: float):
        super(Decibel, self).__init__(val)
        self.validate()
