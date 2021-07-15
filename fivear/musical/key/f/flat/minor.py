"""

    *F♭ Minor*

  The key of F♭ minor.

"""

from ..._mode import MinorKey
from ....scale import Diatonic

from ._key import FfKey

__all__ = ["FfMinor"]


class FfMinor(
    FfKey,
    MinorKey,
    Diatonic,
):
    pass
