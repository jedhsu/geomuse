"""

    *vol*

  Volume types.

"""

from ._bind import Volume

from .amplitude import Amplitude
from .decibel import Decibel

__all__ = [
    "Volume",
    "Amplitude",
    "Decibel",
]

# from .phon import Phon

# from .power import Power

# Ampl.Amplitude = Amplitude
# Ampl.Decibel = Decibel
# Ampl.Power = Power
# Ampl.Phon = Phon

# __all__ = ["Ampl"]
