"""

    *Step Two*

  Of step two.

"""

from abc import ABCMeta
from dataclasses import dataclass

from ._stepped import Stepped

__all__ = ["StepTwo"]


@dataclass
class StepTwo(
    Stepped,
):
    __metaclass__ = ABCMeta
