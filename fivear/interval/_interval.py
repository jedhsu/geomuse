"""

    *Interval*

"""

from abc import ABCMeta
from dataclasses import dataclass

from ._unit import UnitInterval

__all__ = ["Interval"]


@dataclass
class Interval:
    __metaclass__ = ABCMeta

    steps: UnitInterval
