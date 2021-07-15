"""

    *Fourier-Coefficient*

  The fourier coefficient type.

"""

from abc import ABCMeta
from typing import TypeVar

__all__ = ["FourierCoefficient"]


class FourierCoefficient:
    __metaclass__ = ABCMeta

    Alpha = TypeVar("Alpha")
    Beta = TypeVar("Beta")
