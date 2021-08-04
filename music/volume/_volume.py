"""

    *Volume*

  A measure of sound volume.

"""

from abc import ABCMeta

from typing import TypeVar

__all__ = ["Volume"]


class Volume(
    ValueMeasure,
):
    __metaclass__ = ABCMeta

    Amplitude = TypeVar("Amplitude")
    Decibel = TypeVar("Decibel")
    Power = TypeVar("Power")
    Phon = TypeVar("Phon")
