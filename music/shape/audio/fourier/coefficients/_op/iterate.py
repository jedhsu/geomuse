"""

    *Fourier-Coefficients Iterate*

  Iterate over the fourier coefficients.

"""

from .._coefficients import FourierCoefficients

__all__ = ["FourierCoefficientsIterate"]


class FourierCoefficientsIterate:
    def __next__(self):
        ...

    def __iter__(self):
        return self
