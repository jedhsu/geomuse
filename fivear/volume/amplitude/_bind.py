"""

    *Amplitude,   [Bindings]*

"""

from ._amplitude import Amplitude as _Amplitude

from .convert import Convert
from .display import Display

__all__ = ["Amplitude"]


class Amplitude(
    Convert,
    Display,
    _Amplitude,
):
    pass
