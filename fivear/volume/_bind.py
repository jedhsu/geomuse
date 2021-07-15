"""

    *Volume,   [Bindings]*

"""

from ._volume import Volume

from .amplitude import Amplitude
from .decibel import Decibel

__all__ = ["Volume"]

Volume.Amplitude = Amplitude
Volume.Decibel = Decibel
