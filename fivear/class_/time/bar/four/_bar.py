"""

    *Bar Four*

  Of bar four.

"""

from abc import ABCMeta
from dataclasses import dataclass

from .._bar import Bar

__all__ = ["BarFour"]


@dataclass
class BarFour(
    Bar,
):
    __metaclass__ = ABCMeta
