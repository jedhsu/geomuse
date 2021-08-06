"""

    *Absolute Key-Element*

"""

from abc import ABCMeta

from .._element import KeyElement
from ._key import AbsoluteKey

__all__ = ["AbsoluteKeyElement"]


class AbsoluteKeyElement(
    AbsoluteKey,
    KeyElement,
):
    __metaclass__ = ABCMeta
