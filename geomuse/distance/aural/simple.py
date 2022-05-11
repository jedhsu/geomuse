"""

    *Simple Aural Interval*

  An interval that is less than equal to an octave.

  Simple / compound intervals partition by ordering.

"""

from abc import ABCMeta

from ._interval import AuralInterval

__all__ = ["SimpleInterval"]


class SimpleInterval(
    Interval,
):
    __metaclass__ = ABCMeta
