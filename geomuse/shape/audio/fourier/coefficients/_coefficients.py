"""
    
    *Fourier-Coefficients*

  The Fourier coefficients.

"""

__all__ = ["FourierCoefficients"]

from abc import ABCMeta
from dataclasses import dataclass

from typing import Iterator

from .math import Function


@dataclass(frozen=True)
class FourierCoefficients:
    alpha: AlphaCoefficients
    beta: BetaCoefficients


class Coefficients(
    _Iterate_,
    metaclass=ABCMeta,
):
    def __init__(self, fn: Function):
        ...
