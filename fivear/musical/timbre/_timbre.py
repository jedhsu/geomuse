"""

    *Timbre*

  Maps the harmonics of a harmonic series to volume.

  # [TODO] this is theoretically WAVE, move out?

"""

from typing import Mapping

from fivear.frequency import AudioFrequency
from fivear.volume import Volume

from ..harmonic import Harmonic
from ..harmonic import HarmonicSeries


class Timbre(
    HarmonicSeries,
    Mapping[Harmonic, Volume],
):
    def __init__(self):
        pass
