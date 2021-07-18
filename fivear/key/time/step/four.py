"""

    *Step Four*

  Of step four.

"""

from abc import ABCMeta
from dataclasses import dataclass

from ._stepped import Stepped

__all__ = ["StepFour"]


@dataclass
class StepFour(
    Stepped,
):
    __metaclass__ = ABCMeta
