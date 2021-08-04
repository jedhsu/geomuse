"""

    *F♭ Major*

  The key of F♭ major.

"""

from ..._mode import MajorKey
from ....scale import Diatonic

from ._key import FfKey

__all__ = ["FfMajor"]


class FfMajor(
    FfKey,
    MajorKey,
    Diatonic,
):
    pass
