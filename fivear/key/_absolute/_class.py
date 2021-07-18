"""

    *Absolute Key-Class*

"""

from abc import ABCMeta

from .._class import KeyClass
from ._key import AbsoluteKey

__all__ = ["AbsoluteKeyClass"]


class AbsoluteKeyClass(
    AbsoluteKey,
    KeyClass,
):
    __metaclass__ = ABCMeta
