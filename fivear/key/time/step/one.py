"""

    *Step One*

  Of step one.

"""

from abc import ABCMeta
from dataclasses import dataclass

from ._stepped import Stepped

__all__ = ["StepOne"]


@dataclass
class StepOne(
    Stepped,
):
    __metaclass__ = ABCMeta
