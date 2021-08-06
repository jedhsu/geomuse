"""

    *Step Three*

  Of step three.

"""

from abc import ABCMeta
from dataclasses import dataclass

from ._stepped import Stepped

__all__ = ["StepThree"]


@dataclass
class StepThree(
    Stepped,
):
    __metaclass__ = ABCMeta
