"""

    *Unit Interval*

"""

from abc import ABCMeta
from dataclasses import dataclass

# [TODO] think we ned some metric of step distance? use int for now

__all__ = ["UnitInterval"]


@dataclass
class UnitInterval:
    __metaclass__ = ABCMeta
