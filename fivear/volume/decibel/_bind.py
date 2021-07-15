from ._decibel import Decibel as _Decibel

from .convert import Convert
from .display import Display

__all__ = ["Decibel"]


class Decibel(
    Convert,
    Display,
    _Decibel,
):
    pass
