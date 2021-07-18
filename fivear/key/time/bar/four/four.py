"""

    *Four.4*

  Bar four, step four.

"""

from dataclasses import dataclass

from ..step import StepFour
from ._bar import BarFour

__all__ = ["Four4"]


@dataclass
class Four4(
    BarFour,
    StepFour,
):
    pass
