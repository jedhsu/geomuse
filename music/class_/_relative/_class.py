"""

    *Relative Key-Class*

"""

from abc import ABCMeta

from .._class import KeyClass
from ._key import RelativeKey

__all__ = ["RelativeKeyClass"]


class RelativeKeyClass(
    RelativeKey,
    KeyClass,
):
    __metaclass__ = ABCMeta
