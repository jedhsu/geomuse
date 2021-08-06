"""

    *Relative Key-Element*

"""

from abc import ABCMeta

from .._element import KeyElement
from ._key import RelativeKey

__all__ = ["RelativeKeyElement"]


class RelativeKeyElement(
    RelativeKey,
    KeyElement,
):
    __metaclass__ = ABCMeta
