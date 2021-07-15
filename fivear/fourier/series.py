"""

Fourier series, magnitude and phase form.

"""

from dataclasses import dataclass
from typing import Iterator, Sequence

from .coeffs import Coefficients


@dataclass(frozen=True)
class _FourierSeries:
    alpha: Coefficients.Alpha
    beta: Coefficients.Beta


class FourierSeries(Sequence[float]):
    def __init__(self):
        ...
